from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class contact(models.Model):
        Firstname=models.CharField(max_length=100)
        Middlename=models.CharField(max_length=100,default='')
        Lastname=models.CharField(max_length=100,default='')
        EmailId=models.CharField(max_length=100)
        Comments=models.TextField(default='')

        def __str__(self):
                return self.Firstname


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class category(models.Model):
        cname=models.CharField(max_length=40, default='')

        def __str__(self):
                return self.cname

class category1(models.Model):
        cname1=models.CharField(max_length=40, default='')

        def __str__(self):
                return self.cname1

class category2(models.Model):
        cname2=models.CharField(max_length=40, default='')

        def __str__(self):
                return self.cname2

class category3(models.Model):
        cname3=models.CharField(max_length=40, default='')

        def __str__(self):
                return self.cname3

class category4(models.Model):
        cname4=models.CharField(max_length=40, default='')

        def __str__(self):
                return self.cname4