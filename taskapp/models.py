from django.db import models

Gender_choices = [
    ('Male','MALE'),
    ('Female','Female')
]


class Employee(models.Model):
    empname = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=120, unique=True,blank=False,
                              error_messages={'unique':'This Email is Already Exist.'})
    gender = models.CharField(max_length=6,blank=False, choices=Gender_choices)
    status = models.CharField(max_length=7)
    image = models.ImageField(upload_to='images/', blank=False)

