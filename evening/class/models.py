from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name
