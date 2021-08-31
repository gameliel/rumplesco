from django.db import models

# Create your models here.
class Whatsapp(models.Model):
    phone_number = models.CharField(max_length=14)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.phone_number
