# Generated by Django 4.1.5 on 2023-02-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='usertype',
            new_name='user_type',
        ),
    ]