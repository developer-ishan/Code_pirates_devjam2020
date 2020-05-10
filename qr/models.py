from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class gate_entry(models.Model):
    name = models.CharField(max_length=255)
    regno = models.PositiveIntegerField(validators=[MinValueValidator(11111111,'please enter valid registration no'),MaxValueValidator(99999999,'please enter valid registration no')])
    roomno = models.PositiveIntegerField(validators=[MinValueValidator(100,'please enter valid room no'),MaxValueValidator(999,'please enter valid room no')])
    intime = models.DateTimeField(blank = True,null=True)
    outtime = models.DateTimeField(blank = True,null=True)
    #the work of entry can be done by id
    # entry = models.PositiveIntegerField(blank = True,null=True)
    #create entry = id using save method
    class Meta:
        verbose_name = 'gate_entry'
        verbose_name_plural = 'gate_entries'
    
