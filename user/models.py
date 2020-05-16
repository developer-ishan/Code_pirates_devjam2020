from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from communities.models import community
# Create your models here.


class user_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    regno = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(11111111,'please enter valid registration no'),MaxValueValidator(99999999,'please enter valid registration no')])
    branch = models.CharField(max_length=3)
    group = models.CharField(max_length=2)
    roomno = models.PositiveIntegerField(validators=[MinValueValidator(100,'please enter valid room no'),MaxValueValidator(999,'please enter valid room no')])
    hostel = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='static/images/profile_pic',default = 'static/images/profile_pic/avatar.png')
    following = models.ManyToManyField(community,blank = True)
