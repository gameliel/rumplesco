# Generated by Django 3.1.7 on 2021-07-16 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210716_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='necksize',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='store.necksize'),
        ),
    ]
