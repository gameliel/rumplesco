# Generated by Django 3.1.7 on 2021-07-16 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0014_auto_20210716_1151'),
        ('store', '0022_auto_20210716_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='brand_imgs/')),
            ],
            options={
                'verbose_name_plural': '3. Brands',
            },
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amt', models.FloatField()),
                ('paid_status', models.BooleanField(default=False)),
                ('order_dt', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('process', 'In Process'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='process', max_length=150)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '8. Orders',
            },
        ),
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=150)),
                ('item', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cartorder')),
            ],
            options={
                'verbose_name_plural': '9. Order Items',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '4. Colors',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.color')),
            ],
            options={
                'verbose_name_plural': '7. ProductAttributes',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '5. Sizes',
            },
        ),
        migrations.CreateModel(
            name='UserAddressBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AddressBook',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Wishlist',
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '6. Products'},
        ),
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='content',
            new_name='review_text',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_visit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='necksize',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_visits',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='stars',
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productreview',
            name='review_rating',
            field=models.CharField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Necksize',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
        ),
    ]