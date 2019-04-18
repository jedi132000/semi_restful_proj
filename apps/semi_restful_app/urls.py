from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view,  name='view'),
    url(r'^new/$', views.new,  name='new'),
    url(r'^create/$', views.create,  name='create'),
    url(r'^(?P<show_id>\d+)/edit/$', views.edit, name="edit"),
    url(r'^(?P<show_id>\d+)/update/$', views.update, name="update"),
    url(r'^(?P<show_id>\d+)/$', views.display, name="display"),
]

