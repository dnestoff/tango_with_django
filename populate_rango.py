import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
  suits_cat = add_cat('Suits', 32, 125)
  
  add_page(cat=suits_cat,
    title = "Blue suit")

  add_page(cat=suits_cat,
    title = "Georgio Armani")

  add_page(cat=suits_cat,
    title = "Zoot suit")

  pants_cat = add_cat('Pants')

  add_page(cat=pants_cat, title= "Pinstripe")

  add_page(cat=pants_cat, title="Jeans")

  # Print out what we have added for the user
  for c in Category.objects.all():
    for p in Page.objects.filter(category=c):
      print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, views=0):
  page = Page.objects.get_or_create(category=cat, title=title)[0]
  page.url = ''
  page.views = 0
  page.save()
  return page

def add_cat(name, views=0, likes=0):
  cat = Category.objects.get_or_create(name=name)[0]
  cat.views = views
  cat.likes = likes
  return cat

if __name__ == '__main__':
  print("Starting Rango population script...")
  populate()