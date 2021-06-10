from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist, Item
from .forms import CreatenewList, CreateUserFormm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import paho.mqtt.client as mqtt
from random import randrange, uniform
import paho.mqtt.subscribe as subscribe
from django.contrib.auth.decorators import login_required
import time



@login_required(login_url='login')
def index2(response, id):
    ls = Todolist.objects.get(id=id)
    if ls==response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id))=="clicked":
                        item.complete = True
                    else:
                        item.complete = True

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt)>2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("ivalid")


        return render(response, "main/list.html", {"ls":ls})
    else:
        return render(response, "main/view.html", {"ls":ls})


@login_required(login_url='login')
def home(response):


   

    context = {
        
    }
    return render(response, "main/home.html", context)


@login_required(login_url='login')
def site1(response):


   

    context = {
        "Phase1":0,
    }
    return render(response, "main/site1.html", context)


@login_required(login_url='login')
def site2(response):
    context = {
        "Phase1":0,
    }
    return render(response, "main/site2.html", context)


@login_required(login_url='login')
def create(response):
    response.user
    if response.method == "POST":
        form = CreatenewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            
            t = Todolist(name=n)
            t.save()
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" %t.id)

    else: 
        form = CreatenewList()
    
    return render(response, 'main/create.html', {"form":form})

 
@login_required(login_url='login')   
def view(response):
    return render(response, "main/view.html", {})



@login_required(login_url='login')
def sensors(response):
    return render(response, "main/sensors.html", {})


@login_required(login_url='login')
def valuess(response):
    return render(response, "main/valuess.html", {})


def registerpage(response):
    if response.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserFormm()
        if response.method == "POST":
            form = UserCreationForm(response.POST)

            if form.is_valid():
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(response, 'Account creatd for ' + user)
                return redirect('login')

        else: 
            form = CreateUserFormm()

        context = {'form':form}
        return render(response, "main/registerpage.html", context)


def loginpage(response):
    if response.user.is_authenticated:
        return redirect('home')
    else:
        if response.method == "POST":
            username=response.POST.get('username')
            password=response.POST.get('password')
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                return redirect('home')
            else:
                messages.info(response, 'Username or Password is incorrect')

        return render(response, "main/loginpage.html", {})

def logoutuser(request):
    logout(request)
    return redirect('login')
