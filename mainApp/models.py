from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class UserDetail(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="current")
    gender=models.CharField(max_length=100)
    phone= models.CharField(max_length=11, null=True, blank=True, help_text='Contact phone number')
    country=models.CharField(max_length=100, default=None)
    city=models.CharField(max_length=100, default=None)
    state=models.CharField(max_length=100, default=None)
    dob=models.DateField()
    photo=models.FileField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return self.user.username

class PlotHistory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    points=JSONField(default=dict, null=True, blank=True)
