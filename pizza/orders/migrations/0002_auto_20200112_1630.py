# Generated by Django 2.2.9 on 2020-01-12 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servedPizz', '0002_auto_20200112_1500'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='orderPizza',
            new_name='orderPizzaItem',
        ),
    ]
