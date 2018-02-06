import uuid
from shortuuidfield import ShortUUIDField
from django.db import models
from NGO.models import NGO, Children


class Invoice(models.Model):
    select_ngo = models.ForeignKey(NGO, default=1)
    child_name = models.CharField(max_length=100)
    child_code = models.CharField(max_length=6)
    donor_id = models.CharField(max_length=100)
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
    time_stamp = models.DateTimeField(auto_now=True, auto_created=True)


class Donor(models.Model):
    donor_name = models.CharField(max_length=100)
    donor_id = ShortUUIDField(max_length=10, editable=False)
    donor_country = models.CharField(choices=(
        ('us', "USA"),
        ('india', "INDIA"),
        ('aus', "Australia"),
    ), max_length=10
    )
    donor_full_address = models.CharField(max_length=250)
    donor_image = models.ImageField(upload_to='DonorList/')
    joined = models.DateTimeField(auto_now=True)
