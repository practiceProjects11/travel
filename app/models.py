from django.db import models

# Create your models here.
class Destination(models.Model):
    price=models.IntegerField()

    name=models.CharField(max_length=30)

    img=models.ImageField(upload_to='pics')
    offer= models.BooleanField(default=False)


