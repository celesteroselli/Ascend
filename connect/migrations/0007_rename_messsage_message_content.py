# Generated by Django 5.1.3 on 2024-11-16 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0006_alter_message_messsage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='messsage',
            new_name='content',
        ),
    ]
