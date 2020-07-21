from django.db import models
from django.urls import reverse
from django.conf import settings
from datetime import datetime

from accounts.models import User,EmployeeProfile

class PostJob(models.Model):
    company_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.TextField()
    experience = models.PositiveIntegerField()
    keyskills = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postjob:list")

    class Meta:
        ordering = ['-created_at']


class JobApplication(models.Model):
    job = models.ForeignKey(PostJob,on_delete=models.CASCADE,related_name='application')
    user = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(default=1,blank=True,null=True)
    applied_at = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ('job','user')
        ordering = ['-rank']
