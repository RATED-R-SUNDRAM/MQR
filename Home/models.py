from email.headerregistry import Address
from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="contact/images")
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    sex=models.CharField(max_length=255)
    email=models.EmailField()
    address=models.TextField()
    dob=models.DateField()
    mobile=models.IntegerField()
    matrialStatus=models.CharField(max_length=255)
    workplace=models.CharField(max_length=1000)
    designation=models.CharField(max_length=500)
    links=models.TextField()
    slug=models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return "Contact created "+ self.fname

class Medical(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    report=models.ImageField(upload_to="medical/images")
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    sex=models.CharField(max_length=255)
    email=models.EmailField()
    mobile=models.IntegerField()
    height=models.CharField(max_length=255)
    weight=models.CharField(max_length=255)
    bgroup=models.CharField(max_length=10)
    problem=models.TextField()
    doctor=models.CharField(max_length=1000)
    history=models.TextField()
    slug=models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return "Report created "+ self.fname

class Resume(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="resume/images")
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    sex=models.CharField(max_length=255)
    email=models.EmailField()
    address=models.TextField()
    mobile=models.IntegerField()
    experiace=models.TextField()
    matrialStatus=models.CharField(max_length=255)
    workplace=models.CharField(max_length=1000)
    designation=models.CharField(max_length=500)
    links=models.TextField()
    slug=models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return "Resume created "+ self.fname

class QR(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="QR")
    slug=models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return "QR created "
        