from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Connection(models.Model):
    astronaut = models.ForeignKey(User, on_delete=models.CASCADE, related_name='astro', unique=False)
    earthling = models.ForeignKey(User, on_delete=models.CASCADE, related_name='earth', unique=False)

class Message(models.Model):
    msg_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_from', unique=False)
    msg_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_to', unique=False)
    video = models.FileField(blank=False, unique=False)
    content = models.CharField(max_length=50, blank=False, unique=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()