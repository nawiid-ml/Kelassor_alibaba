from django.db import models

class Bus_Ticket(models.Model):
    Bus_Name=models.CharField(max_length=250)
    Origin=models.CharField(max_length=200)
    Destination=models.CharField(max_length=250)
    Date_Of_Departure=models.DateField()
    Time_Of_Departure=models.TimeField()
    Description=models.TextField()


class Terminal(models.Model):
    Name=models.CharField(max_length=250)
    City=models.CharField(max_length=200)
    Address=models.TextField()
    Phone_Number=models.IntegerField()
    open_time=models.TimeField()
    close_time=models.TimeField()


    

