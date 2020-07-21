from django.urls import path
from accounts import views


app_name = 'accounts'


urlpatterns = [
        path('employeesignup',views.employee_signup,name='employeesignup'),
        path('employersignup',views.employer_signup,name='employersignup'),
        path('login',views.user_login,name='login'),
        path('logout',views.user_logout,name='logout'),
]
