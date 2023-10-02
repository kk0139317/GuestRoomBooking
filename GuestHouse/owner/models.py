from django.db import models

# Create your models here.

class OwnerList(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)


class Visitor(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)

class RoomData(models.Model):
    title = models.CharField(max_length=50)
    room_id = models.CharField(max_length=15)
    floor = models.IntegerField()
    bed = models.IntegerField()
    bathroom = models.IntegerField()
    location = models.TextField()
    about = models.TextField(null=True)
    desc = models.TextField()
    prize = models.IntegerField()
    wifi = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/')
    updated_by = models.CharField(max_length=30, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

class Contact(models.Model):
    username = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.email
    

class BookingData(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    room_id = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    checkin = models.DateField()
    checkout = models.DateField()
    adult = models.IntegerField()
    chield = models.IntegerField()
    message = models.TextField()
    owner = models.CharField(max_length=30)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
