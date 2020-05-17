from django.db import models

# Create your models here.


weekdays = [
        ('MONDAY', 'MONDAY'),
        ('TUESDAY', 'TUESDAY'),
        ('WEDNESDAY', 'WEDNESDAY'),
        ('THRUSDAY', 'THRUSDAY'),
        ('FRIDAY', 'FRIDAY'),
        ('SATURDAY', 'SATURDAY'),
        ('SUNDAY', 'SUNDAY'),
    ]
class doc(models.Model):
    name = models.CharField(max_length=255)
    spec = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class timing(models.Model):
    doc = models.ForeignKey(doc,on_delete=models.CASCADE,null=True)
    day = models.CharField(max_length=15,choices = weekdays)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    # time = models.ForeignKey(timing,on_delete=models.CASCADE)
