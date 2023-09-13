from django.db import models

class hbalances(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    date = models.DateField(max_length=30)
    status = models.CharField(default="PROCESSED",max_length=30)