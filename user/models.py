from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.


class user_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    regno = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(11111111,'please enter valid registration no'),MaxValueValidator(99999999,'please enter valid registration no')])
    # todo: make this a select from dropdown 
    branch = models.CharField(max_length=3)
    group = models.CharField(max_length=2)
    roomno = models.PositiveIntegerField(validators=[MinValueValidator(100,'please enter valid room no'),MaxValueValidator(999,'please enter valid room no')])
    #todo: make this a select field from dropdown
    hostel = models.CharField(max_length=255)
