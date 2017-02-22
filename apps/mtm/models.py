from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def add_entry(self, addData):
        user_query = User.objects.filter(fname = addData['fname'], lname = addData['lname'])
        interest_query = Interest.objects.filter(name = addData['interest'])
        if not user_query and len(addData['fname']) > 0 and len(addData['lname']) > 0:
            User.objects.create(fname = addData['fname'], lname = addData['lname'])
        else:
            print "Already in database!"
        if not interest_query:
            Interest.objects.create(name = addData['interest'])
        else:
            print "Already in database!"
        try:
            User.objects.get(fname = addData['fname'], lname = addData['lname']).interests.add(Interest.objects.get(name = addData['interest']))
        except:
            pass
class User(models.Model):
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Interest(models.Model):
    name = models.CharField(max_length = 255)
    users = models.ManyToManyField(User, related_name = "interests")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
