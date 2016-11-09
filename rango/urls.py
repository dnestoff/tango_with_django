from django.conf.urls import url
from rango import views

# urlpatterns = [url(matching_criteria, location_of_view, optional_arg)]

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^about/', views.about, name = 'about'), 
  url(r'^contact/', views.contact, name = 'contact')
]