from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User
from my_social_network.models import UserLink

# Create your views here.
def users (request):
  user_list=User.objects.all()
  t= loader.get_template('my_social_network/users.html')
  c= Context({'user_list':user_list,})
  return HttpResponse(t.render(c))

def follower (request, username):
  follower_list=UserLink.objects.filter(to_user__username=username)
  t= loader.get_template('my_social_network/followers.html')
  c= Context({'user_list':follower_list,})
  return HttpResponse(t.render(c))

def following (request, username):
  following_list=UserLink.objects.filter(from_user__username=username)
  t= loader.get_template('my_social_network/following.html')
  c= Context({'user_list':following_list,})
  return HttpResponse(t.render(c))