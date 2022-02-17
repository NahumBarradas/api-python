from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Event(models.Model):
    class StateChoice(models.TextChoices):
        Alabama = 'Alabama, AL'
        Alaska = 'Alaska, AK'
        Arizona = 'Arizona, AZ'
        Arkansas = 'Arkansas, AR'
        California = 'California, CA'
        Colorado = 'Colorado, CO'
        Connecticut = 'Connecticut, CT'
        Delaware = 'Delaware, DE'
        Tennessee = 'Tennessee, TN'
        Texas = 'Texas, TX'
        Utah = 'Utah, UT'
        Vermont = 'Vermont, VT'
        Virginia = 'Virginia, VA'
        Washington = 'Washington, WA'
        West_Virginia = 'West_Virginia, WV'
        Wyoming = 'Wyoming, WY'

    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100, choices=StateChoice.choices, default=StateChoice.Alabama)
    zipcode = models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)
    end_date = models.DateField(max_length=100)
    category = models.CharField(max_length=100)
    list_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        verbose_name_plural = 'app'

    def __str__(self):
        return self.title