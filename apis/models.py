from django.db import models

# Create your models here.


class Member(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)


class Activity(models.Model):
    member = models.ForeignKey(
        Member, related_name='activities', null=True, on_delete=models.SET_NULL)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(blank=True, null=True)
