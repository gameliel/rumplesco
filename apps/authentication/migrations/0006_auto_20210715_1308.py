# Generated by Django 3.1.7 on 2021-07-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210715_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hip_size',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Medium')], default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='neck_size',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Medium'), (2, 'Large')], default=0),
        ),
    ]
