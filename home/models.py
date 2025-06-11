from django.db import models


# Create your models here.

class BookingData(models.Model):
    sender_name = models.CharField(max_length=20)
    sender_phone = models.CharField(max_length=20)
    sender_address = models.CharField(max_length=20)
    sender_station = models.CharField(max_length=20)
    reciever_name = models.CharField(max_length=20)
    reciever_phone = models.CharField(max_length=20)
    reciever_address = models.CharField(max_length=20)
    reciever_station = models.CharField(max_length=20)
    awbno = models.CharField(max_length=20)
    pcs = models.CharField(max_length=5)
    wt = models.CharField(max_length=5)


class TransitDetails(models.Model):
    date = models.DateField()
    station = models.CharField(max_length=30)
    activitylist = models.CharField(max_length=30)
    awbno=models.CharField(max_length=20)


class Destinations(models.Model):
    name = models.CharField(max_length=30)