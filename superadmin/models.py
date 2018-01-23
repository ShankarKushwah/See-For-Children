from django.db import models
from NGO.models import NGO, Children


class Invoice(models.Model):
    select_ngo = models.ForeignKey(NGO, default=1)
    child_name = models.ForeignKey(Children, default=1)
    donor_id = models.CharField(max_length=100)
    invoice = models.FileField(blank=True)
    donation_month = models.CharField(choices=(
        ('jan', "January",),
        ('feb', "February"),
        ('mar', "March"),
        ('apr', "April"),
        ('may', "May"),
        ('jun', "June"),
        ('jul', "July"),
        ('aug', "August"),
        ('sep', "September"),
        ('oct', "October"),
        ('nov', "November"),
        ('dec', "December"),
    ), max_length=10
    )
    date = models.DateField()
    paid = models.CharField(max_length=10)


