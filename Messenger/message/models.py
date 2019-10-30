from django.db import models

# Create your models here.

class Messages(models.Model):
    text = models.TextField()
    sender = models.IntegerField()
    receiver = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1) # 1: send 2: receive 3: seen
