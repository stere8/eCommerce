import uuid
from django.db import models
import datetime
from django.conf import settings

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=120)
    id = models.AutoField(
         primary_key=True,
         editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"




class product(models.Model):
    name = models.CharField(max_length=120)
    #seller = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    category = models.OneToOneField(category,null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(default='Default')
    id = models.AutoField(
        primary_key=True,
        editable=False)
    price = models.IntegerField(blank=False)
    dateadded = models.DateField(auto_created=True, default=datetime.date.today(),blank=False)
    visits = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.name


class image(models.Model):
    rproduct = models.ForeignKey(product,on_delete=models.CASCADE,null=False, blank=False)
    path = models.ImageField(upload_to='images/')
    id = models.AutoField(
        primary_key=True,
        editable=False)
    descpription = models.TextField()

    def __str__(self):
        return str(self.id) + str(self.rproduct.name)
