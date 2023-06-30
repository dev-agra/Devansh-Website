from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length= 20,blank=False)
    phoneno = models.CharField(max_length=25)
    proname = models.CharField(max_length=25)
    prodesp = models.CharField(max_length=50)
    proquote = models.CharField(max_length=10)

class Feedback(models.Model):
    proid = models.CharField(max_length= 15, null=False, blank=False)
    proname = models.CharField(max_length=30)
    prodate = models.DateField()
    prorate = models.IntegerField()
    proexp = models.CharField(max_length=50)
    prosuggest = models.CharField(max_length=50)
