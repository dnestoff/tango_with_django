from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.models import Category, Page 
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

def index(request):
    categories = Category.objects.order_by('-name')[:5]
    pages = Page.objects.order_by('-views')[:5]
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'categories': categories, 'pages': pages }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, "rango/index.html", context_dict)

def about(request):
    return render(request, "rango/about.html")


def contact(request):
    context_dict = {'email': "myemail@email.com", 'username': "ronaldWasHere", 'age': 23}

    return render(request, "rango/contact.html", context_dict)

def register(request):
    # set to true if a success
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # save the user info then hash password
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # create unpersisted UserProfile for linking to User
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            # switch to True after success
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else: 
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def category(request, category_name_url):
    context_dict = {}

    try:
        # If we can't find category, the .get() method raises DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug = category_name_url)
        context_dict['category'] = category
        context_dict['category_name'] = category.name
        context_dict['category_slug'] = category_name_url

        context_dict['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        pass

    return render(request, "rango/category.html", context_dict)

# below process both GET and POST requests
def add_category(request):
    # a POST request?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, "rango/add_category.html", {'form': form})

def page(request, page_name_url):
    context_dict = {}

    try:
        # If we can't find category, the .get() method raises DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        page = Page.objects.get(slug = page_name_url)
        context_dict['page'] = page
        context_dict['page_title'] = page.title

    except Page.DoesNotExist:
        pass

    return render(request, "rango/page.html", context_dict)

def add_page(request, category_name_url):
    
    try: 
        category = Category.objects.get(slug = category_name_url)
    except Category.DoesNotExist:
                category = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(category)
                # return redirect('/rango/category/'+category.slug+'/')

        else:
            print(form.errors)
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': category}

    return render(request, "rango/add_page.html", context_dict)