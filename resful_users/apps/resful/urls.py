from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^users$',views.index),
    url(r'^users/new$',views.new),
    url(r'^users/create$',views.create),
    url(r'^users/(?P<user_id>\d+)$',views.display),
    url(r'^users/edit/(?P<user_id>\d+)$',views.edit),
    url(r'^users/update/(?P<user_id>\d+)$',views.update),
    url(r'^users/(?P<user_id>\d+)/alert$',views.alert),
    url(r'^users/(?P<user_id>\d+)/destroy$',views.destroy),
]