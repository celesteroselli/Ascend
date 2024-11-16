from django.db import models
from django.contrib.auth.models import User

class Connection(models.Model):
    astronaut = models.ForeignKey(User, on_delete=models.CASCADE, related_name='astro', unique=False)
    earthling = models.ForeignKey(User, on_delete=models.CASCADE, related_name='earth', unique=False)

class Message(models.Model):
    msg_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_from', unique=False)
    msg_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_to', unique=False)
    video = models.FileField(blank=False, unique=False)
    content = models.CharField(max_length=50, blank=False, unique=False)