from django.db import models

class Product(models.Model):
   name        = models.CharField(max_length=200)
   pictureURL  = models.ImageField(upload_to='images')

   def __unicode__(self):
      return self.name


class User(models.Model):
   firstName   = models.CharField(max_length=200)
   lastName    = models.CharField(max_length=200)
   address     = models.CharField(max_length=200)
   cep         = models.IntegerField()    

   def __unicode__(self):
      return self.firstName + ' ' + self.lastName

