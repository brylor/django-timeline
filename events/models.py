from django.contrib import admin
from django.db import models
import datetime
from datetime import date
from django.utils.dates import MONTHS
import math
# Create your models here.



class Event(models.Model):
    title  = models.CharField(max_length=200)
    #start_date = models.DateField('start date', default=date.today)
    #end_date = models.DateField('end date', default=date.today)

    JULIAN_RECKONING=(
      ('AD','anno Domini'),
      ('BC','before Christ'),
    )

    julian_start = models.CharField('Julian Start',max_length=2,choices=JULIAN_RECKONING,default='AD')
    julian_end = models.CharField('Julian End',max_length=2,choices=JULIAN_RECKONING,default='AD')

    start_year = models.IntegerField(('Start Year'), default=datetime.datetime.now().year)
    end_year = models.IntegerField(('End Year'), default=datetime.datetime.now().year)

    start_month = models.IntegerField(('Start Month'), default='00',choices=MONTHS.items())
    end_month = models.IntegerField(('End Month'), default='00',choices=MONTHS.items())

    start_day = models.IntegerField(('Start Day'), default=datetime.datetime.now().day)
    end_day = models.IntegerField(('End Day'), default=datetime.datetime.now().day)

    def __str__(self):
       return self.title

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_year','start_month','start_day','end_year','end_month')

    def leading_zeros(value, desired_digits):
        return str(value).zfill(desired_digits)

    def save_model(self, request, obj, form, change):
        #self.start_year = self.leading_zeros(self.start_year,4)
        if obj.julian_start == 'BC':
            start_year = -obj.start_year
            print(start_year)
            obj.start_year = start_year
            obj.save()
        if obj.julian_end == 'BC':
            end_year = -obj.end_year
            print(end_year)
            obj.end_year = end_year
            obj.save()
        super().save_model(request, obj, form, change)
