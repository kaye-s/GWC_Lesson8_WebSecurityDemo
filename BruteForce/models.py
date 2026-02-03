from django.db import models


class Login(models.Model):
    password = models.CharField(max_length=100)


def __str__(self):
    return self.password

# Create your models here.
