# Generated by Django 5.1.3 on 2024-11-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_message_messsage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messsage',
            field=models.CharField(max_length=50),
        ),
    ]
