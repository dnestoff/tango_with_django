from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category 

def index(request):
    categories = Category.objects.order_by('-name')[:5]
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context", 'categories': categories}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, "rango/index.html", context_dict)

def about(request):
    return render(request, "rango/about.html")


def contact(request):
    context_dict = {'email': "myemail@email.com", 'username': "ronaldWasHere", 'age': 23}

    return render(request, "rango/contact.html", context_dict)