from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager

class User(AbstractUser):

    username = None
    ROLE_CHOICES = (('employer','employer'),
            ('employee','employee'))

    email = models.EmailField(unique=True,blank=False,error_messages={'unique':"Email already exists.Use another Email"})
    role = models.CharField(max_length=100,choices=ROLE_CHOICES)
    phone_number = models.PositiveIntegerField(blank=True,null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

class EmployerProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()
    keyskills = models.TextField(max_length=500)
    location = models.CharField(max_length=100)

    cv_file = models.FileField(upload_to='cv_folder',blank=True)

    def __str__(self):
        return self.user.email
