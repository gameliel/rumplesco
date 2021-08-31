from django.db import models
from django.contrib.auth.models import AbstractUser, User
from PIL import Image
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import OneToOneField


# Create your models here.
class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images/profile')
    bio = models.CharField(blank=True, max_length=500)
    phone_number = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)