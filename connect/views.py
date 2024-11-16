from django.shortcuts import render
from .models import *
import cv2 
import numpy as np

def home(request):
    connections = Connection.objects.filter(astronaut=request.user)
    return render(request, "base.html", {"connections":connections})

def connection(request, connection):
    this_connection = Connection.objects.get(id=connection)
    messages = Message.objects.filter(connection=this_connection)
    return render(request, "base.html", {"messages":messages})