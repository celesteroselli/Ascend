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
    list1 = [1, 2, 3, 4, 5]
    dates1 = ["10/3/22", "3/14/19", "5/12/17", "9/17/23", "12/20/13"]
    randomnum = (random.choice(list1))
    date = dates1[randomnum-1]
    print(randomnum)
    image = os.path.join(BASE_DIR,str("media/images/"+str(randomnum))+".jpg/")
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
    return render(request, "picture.html", {"connections":connections, "image_url":image, "date":date, "bg":bg, "form":form})

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
    earthling=User.objects.get(username=username)
    message1 = Message.objects.filter(Q(msg_to=earthling)|Q(msg_from=earthling))
    message2 = Message.objects.filter(Q(msg_to=request.user)|Q(msg_from=request.user))
    messages = message1.intersection(message2).order_by('-id')
    return render(request, "videoview.html", {"messages":messages, "form": form})