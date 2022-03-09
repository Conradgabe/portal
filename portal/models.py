from django.db import models


class comment(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20, null=True)
    email_address = models.EmailField(max_length=70, blank=False, null=True)
    matric_number = models.SlugField(max_length=10, null=True)
    home_address = models.CharField(max_length=50, null=True)
    next_of_kin = models.CharField(max_length=20, null=True)
    phone_number = models.IntegerField(null=True)


    def __str__(self):
        return self.firstname
       