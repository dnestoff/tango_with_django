from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page 

def index(request):
    categories = Category.objects.order_by('-name')[:5]
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'categories': categories}

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
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug = category_name_url)
        context_dict['category_name'] = category.name

        context_dict['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        pass

    return render(request, "rango/category.html", context_dict)
