from django.conf.urls import url
from rango import views

# urlpatterns = [url(matching_criteria, location_of_view, optional_arg)]

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^about/$', views.about, name = 'about'), 
  url(r'^contact/$', views.contact, name = 'contact'),
  # <category_name_url> names the parameter
  url(r'^category/(?P<category_name_url>[\w\-]+)/$', views.category, name = 'category'),
  url(r'^page/(?P<page_name_url>[\w\-]+)/$', views.page, name = 'page')
]