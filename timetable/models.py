from django.db import models

# Create your models here.
class Subject(models.Model):
    subject     = models.CharField(max_length = 20)
    start_time  = models.TimeField()
    end_time    = models.TimeField()

    class Meta:
        unique_together = ('subject','start_time')

    def __str__(self):
        return f'{self.subject}____________{self.start_time}-{self.end_time}'

class Day(models.Model):
    group   = models.CharField(max_length = 2)
    day_choices = (
            ('monday','monday'),
            ('tuesday','tuesday'),
            ('wednesday','wednesday'),
            ('thursday','thursday'),
            ('friday','friday'),
            ('saturday','saturday'),
            ('sunday','sunday')
        )
    day_name = models.CharField(max_length = 20,choices=day_choices)
    subjects = models.ManyToManyField(Subject,verbose_name="list of subjects")
    

    def __str__(self):
        return f'{self.group}---{self.day_name}'

class Time_Table(models.Model):
    group   = models.CharField(max_length = 2)
    days    = models.ManyToManyField(Day,verbose_name="list of days")

    def __str__(self):
        return self.group

