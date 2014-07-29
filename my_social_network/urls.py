from django.conf.urls import patterns, url
from my_social_network import views

urlpatterns = patterns('',
                       url(r'^$', views.users, name='users'),
                       url(r'^(?P<username>\w+)/followers/$', views.follower, name='follower'),
                       url(r'^(?P<username>\w+)/following/$', views.following, name='following'),
)