from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    prep_time = models.Field()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name
