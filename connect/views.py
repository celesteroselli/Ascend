from django.shortcuts import render
from .models import *
import numpy as np
import random
from .forms import *

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
        else:
            print("invalid")
            print(form.errors)
    return render(request, "message_create_form.html", {"form": form})

def home(request):
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomnum = (random.choice(list1))
    print(randomnum)
    image = str("images/"+str(randomnum))
    print(image)
    connections = Connection.objects.filter(astronaut=request.user)
    return render(request, "base.html", {"connections":connections, "image_url":image})

def connection(request, connection):
    this_connection = Connection.objects.get(id=connection)
    messages = Message.objects.filter(connection=this_connection)
    return render(request, "base.html", {"messages":messages})