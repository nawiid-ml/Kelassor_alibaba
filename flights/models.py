from django.db import models

# Create your models here.
class Airport (models.Model):
    Name=models.CharField(max_length=250)
    No=models.CharField(max_length=20)
    City=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Phone_Number=models.IntegerField()
    open_time=models.CharField(max_length=100)
    close_time=models.CharField(max_length=100)


class flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    flight_number=models.IntegerField()
    seat=models.IntegerField()
    price=models.IntegerField()


