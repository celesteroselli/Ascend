from django.db import models
from django.contrib.auth.models import User

class Connection(models.Model):
    astronaut = models.OneToOneField(User, on_delete=models.CASCADE, related_name='astro')
    earthling = models.OneToOneField(User, on_delete=models.CASCADE, related_name='earth')

class Message(models.Model):
    msg_from = models.OneToOneField(User, on_delete=models.CASCADE, related_name='msg_from')
    msg_to = models.OneToOneField(User, on_delete=models.CASCADE, related_name='msg_to')
    video = models.FileField()