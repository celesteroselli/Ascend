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

def video(request, username):
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
            return redirect(reverse("home"))
        else:
            print("invalid")
            print(form.errors)
    return render(request, "message_create_form.html", {"form": form})

def home(request):
    list1 = [1, 2, 3, 4, 5]
    dates1 = ["10/3/22", "3/14/19", "5/12/17", "9/17/23", "12/20/13"]
    randomnum = (random.choice(list1))
    date = dates1[randomnum-1]
    print(randomnum)
    image = os.path.join(BASE_DIR,str("media/images/"+str(randomnum))+".jpg/")
    print(image)

    connections = Connection.objects.filter(astronaut=request.user)
    return render(request, "base.html", {"connections":connections, "image_url":image, "date":date})

def connection(request, username):
    this_connection = Connection.objects.get(earthling=User.objects.get(username=username))
    messages = Message.objects.filter(Q(msg_to=this_connection.earthling)|Q(msg_from=this_connection.earthling))
    return render(request, "videoview.html", {"messages":messages})