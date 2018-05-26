# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from . models import *

# Create your views here.
def index(request):# step 1 just render the page
   

    user=User.objects.all()
    context={
        'users' :user,
        
    }

    return render(request, 'resful/index.html',context)
    

def new(request): #step# 2 open the new html page and render it. 
    return render(request, 'resful/users.html')

def create(request): #step #3  get the post request from form and redirect to urls users. which is rendering the index funcation.
   
    users=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
   
    # We can create the session after creating the variable in this example after creating the user in database than I add user Id in my session
    request.session['id'] = users.id 
    return redirect('/users')

def display(request,user_id):
    user=User.objects.get(id=user_id)
    context={
        'users' :user,
    }
    print(context)
    return render(request, 'resful/show.html',context)

def edit(request,user_id):
    user=User.objects.get(id=user_id)
    
    context={
        'users' :user,

    }
    print(context)
    return render(request, 'resful/edit.html',context)
def update(request,user_id):
    users=User.objects.get(id=user_id)
    users.first_name = request.POST['first_name']
    users.last_name = request.POST['last_name']
    users.email = request.POST['email']
    users.save()
    return redirect('/users')



def alert(request,user_id):
    users=User.objects.get(id=user_id)
    
    if users == users:
        worring = "Are you sure you want to delete the following User"
        sure = "Yes! I want to delete this"
        sure_not= 'No'
        context={
            'user':users,
            'aleart':worring,
            'Yes':sure,
            'No':sure_not
            }
    
    return render(request, 'resful/delete.html',context)


def destroy(request,user_id):
    users=User.objects.get(id=user_id)
    users.delete()
    return redirect('/users')