from django.db import models
from django.contrib.auth.models import User

class Connection(models.Model):
    astronaut = models.OneToOneField(User, on_delete=models.CASCADE)
    earthling = models.OneToOneField(User, on_delete=models.CASCADE)

