from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(
        max_length=100,
        unique=True)
    password = models.CharField(max_length=1000)
    avatar = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    token = models.UUIDField(null=True)


    def get_full_name(self):
        return self.firstname + ' ' + self.lastname

