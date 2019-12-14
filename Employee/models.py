from django.db import models

class Employee(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    first_name = models.CharField(max_length=255, blank=True,db_index=True)
    last_name = models.CharField(max_length=255, blank=True,db_index=True)
    email = models.CharField(max_length=100, null=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    gender = models.CharField(max_length=1, null=True, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    address_1 = models.CharField(max_length=128, blank=True, null=True,db_index=True)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    zip_code = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
