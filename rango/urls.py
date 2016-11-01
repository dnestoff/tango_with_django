from django.conf.urls import url
from rango import views

# urlpatterns = patterns('', url(matching_criteria, location_of_view, optional_arg))

urlpatterns = [url(r'^$', views.index, name = 'index')
]