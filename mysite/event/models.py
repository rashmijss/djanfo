from django.db import models

# Create your models here.
class Fruits(models.Model):
    name=models.CharField(max_length=10)
    def _str_ (self):
        return self.name
    class Student (models.Model):
        name=models.CharField(max_length=10)
class Student(models.Model):
    name=models.CharField(max_length=22)
    Student=models.CharField(max_length=10)
    selected=models.BooleanField(default=False)
    def _str_(self):
        return self.name
        
