from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User,EmployerProfile,EmployeeProfile

class EmployeeUserForm(UserCreationForm):
    class Meta:
        fields = ('email','first_name','last_name','password1','password2','phone_number')
        model = User

    def __str__(self):
        return self.email



class EmployeeProfileForm(forms.ModelForm):

    class Meta:
        fields = ('experience','keyskills','location','cv_file')
        model = EmployeeProfile

    def __str__(self):
        return self.email


class EmployerUserForm(UserCreationForm):
    class Meta:
        fields = ('email','first_name','last_name','password1','password2','phone_number')
        model = User

    def __str__(self):
        return self.email
