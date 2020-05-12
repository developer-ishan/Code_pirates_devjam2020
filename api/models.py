from django.db import models
from user.models import User

class entry_status(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    show_tick = models.BooleanField(default=False)
    is_opening_entry = models.BooleanField(default=True)
    
# Create your models here.
