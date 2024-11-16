from django.contrib import admin

from .models import Connection, Message, Profile

# ...
admin.site.register(Connection)
admin.site.register(Message)
admin.site.register(Profile)