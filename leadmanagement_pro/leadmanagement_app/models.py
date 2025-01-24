from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    STATUS_OPTIONS = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Converted', 'Converted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='New')
    SOURCE_OPTIONS = [
        ('Online', 'Online'),
        ('Referral', 'Referral'),
        ('Event', 'Event'),
        ('Advertisement', 'Advertisement'),
    ]
    source = models.CharField(max_length=20, choices=SOURCE_OPTIONS, default='Online')