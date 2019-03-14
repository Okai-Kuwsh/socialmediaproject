from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Interest(models.Model):
    name = models.TextField(max_length=100)#
    type = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    dob = models.DateField(default=False)#These are all attributes to do with the Profile object
    gender = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    interests = models.ManyToManyField(
        to=Interest,
        symmetrical=False
    )

class Member(User):#object
    username = models.TextField(max_length=100)#These are all attributes to do with the Member object
    password = models.TextField(max_length=100)
    profile = models.OneToOneField(
        to=Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

