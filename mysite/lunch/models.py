from django.db import models

AFFORDABILITY_CHOICES = [
    ('affordability1', 'Cheap'),
    ('affordability2', 'Won’t break the bank'),
    ('affordability3', 'Expensive'),
    ('affordability4', 'Crazy expensive'),
    ]


YES_NO_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
    ]


# Create your models here.
class Restaurant (models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    address = models.CharField(max_length=200)
    type_of_food = models.CharField(max_length=200)
    affordability = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    dine_in = models.CharField(max_length=50)
    take_out = models.CharField(max_length=50)
    google_maps_code = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')



