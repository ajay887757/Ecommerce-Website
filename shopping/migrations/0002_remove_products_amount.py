# Generated by Django 3.0.2 on 2020-03-06 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='amount',
        ),
    ]