from django.db import models
from django.contrib import admin

# TODO: modern / international fields

class Demographic(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    gender = models.TextField()
    marital_status = models.TextField() 
    date_of_birth = models.DateField()
    address_line1 = models.TextField()
    address_line2 = models.TextField() 
    state =  models.TextField()
    postal_code = models.TextField()
    phone = models.TextField()
    city = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


admin.site.register(Demographic)
