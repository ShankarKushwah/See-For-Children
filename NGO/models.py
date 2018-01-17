import uuid
from django.db import models


class NGO(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    established = models.DateField()
    no_of_children = models.CharField(max_length=5)
    area = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    director = models.CharField(max_length=30)
    no_of_staff = models.CharField(max_length=5)
    image = models.FileField(upload_to='ngo/')

    def __str__(self):
        return self.name + " " + self.city


class Children(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    code = models.UUIDField(max_length=3, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    place_found = models.CharField(max_length=100)
    gender = models.CharField(choices=(
        ('m', "Male"),
        ('f', "Female")
    ),
        max_length=1
    )
    image = models.ImageField(upload_to='children/', blank=True)
    education = models.CharField(max_length=5, blank=True)
    school = models.CharField(max_length=50, blank=True)
    hobby = models.CharField(max_length=20, blank=True)
    adoption_date = models.DateField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/', blank=True)
    organizer = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " " + self.place


class Staff(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='staff/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name