from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page 
from rango.forms import CategoryForm

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

def category(request, category_name_url):
    context_dict = {}

    try:
        # If we can't find category, the .get() method raises DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug = category_name_url)
        context_dict['category'] = category
        context_dict['category_name'] = category.name

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

