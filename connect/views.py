from django.shortcuts import render, redirect
from .models import *
import random
from .forms import *
from django.urls import reverse
from django.db.models import Q
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from django.views.generic.edit import CreateView

def home(request):
    list1 = [1, 2, 3, 4, 5, 6]
    dates1 = ["11/15/24", "11/15/24", "11/16/24", "11/16/24", "11/17/24", "11/17/24"]
    randomnum = (random.choice(list1))
    date = dates1[randomnum-1]
    print(randomnum)
    image = os.path.join(BASE_DIR,str("media/images/"+str(randomnum))+".JPEG/")
    print(image)
    bg = request.user.profile.image

    form = ChangeImage(instance=Profile.objects.get(user=request.user))
    if request.method == 'POST':
        form = ChangeImage(request.POST,request.FILES, instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            change = form.save()
            request.user.profile.image = change.image
            change.save()
            print("valid")
            print(request.user.profile.image)
            return redirect('home')
        else:
            print("invalid")
            print(form.errors)

    connections = Connection.objects.filter(astronaut=request.user)
    return render(request, "picture.html", {"connections":connections, "image_url":image, "date":date, "bg":bg, "cform":form})

def connection(request, username):
    form = MessageForm(request.POST or None)
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.msg_from = request.user
            print(message.msg_from)
            message.msg_to = User.objects.get(username=username)
            print(message.msg_to)
            message.save()
            print("valid")
        else:
            print("invalid")
            print(form.errors)
    bg = request.user.profile.image

    form2 = ChangeImage(instance=Profile.objects.get(user=request.user))
    if request.method == 'POST':
        form2 = ChangeImage(request.POST,request.FILES, instance=Profile.objects.get(user=request.user))
        if form2.is_valid():
            change = form2.save()
            request.user.profile.image = change.image
            change.save()
            print("valid")
            print(request.user.profile.image)
            return redirect('home')
        else:
            print("invalid")
            print(form2.errors)


    earthling=User.objects.get(username=username)
    message1 = Message.objects.filter(Q(msg_to=earthling)|Q(msg_from=earthling))
    message2 = Message.objects.filter(Q(msg_to=request.user)|Q(msg_from=request.user))
    messages = message1.intersection(message2).order_by('-id')
    return render(request, "videoview.html", {"messages":messages, "form": form, "bg":bg, "cform": form2})