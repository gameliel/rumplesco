# Generated by Django 3.1.7 on 2021-07-16 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20210716_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='accept_alteration',
        ),
    ]