# Generated by Django 4.1.4 on 2022-12-20 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Message',
            new_name='message',
        ),
    ]