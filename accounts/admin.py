from django.contrib import admin
from accounts.models import User,EmployerProfile,EmployeeProfile
# Register your models here.
admin.site.register(User)
admin.site.register(EmployerProfile)
admin.site.register(EmployeeProfile)
