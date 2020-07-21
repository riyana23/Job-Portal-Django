from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.forms import EmployeeUserForm, EmployeeProfileForm, EmployerUserForm

def employee_signup(request):
    registered = False

    if request.method == 'POST':
        user_form = EmployeeUserForm(data=request.POST)
        profile_form = EmployeeProfileForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save(commit=False)
            user.role = 'employee'
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'cv_file' in request.FILES:
                profile.cv_file = request.FILES['cv_file']
            profile.save()

            registered = True
            return redirect('accounts:login')

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = EmployeeUserForm()
        profile_form = EmployeeProfileForm()

    return render(request, 'accounts/employee_signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def employer_signup(request):
    registered = False
    if request.method == 'POST':
        user_form = EmployerUserForm(data=request.POST)

        if user_form.is_valid:
            user = user_form.save(commit=False)
            user.role = 'employer'
            user.save()
            registered = True
            return redirect('accounts:login')
        else:
            return HttpResponse("Error while signing up")
    else:
        user_form = EmployerUserForm()

    return render(request, 'accounts/employer_signup.html', {'user_form': user_form, 'registered': registered})


@login_required(login_url=reverse_lazy('accounts:login'))
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('thanks'))


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('postjob:list'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            return HttpResponse("Invalid Login Details")
    else:
        return render(request, 'accounts/login.html', {})
