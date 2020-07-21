from django.shortcuts import render, redirect

from operator import itemgetter
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from postjob.models import PostJob, JobApplication
from accounts.models import EmployeeProfile, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)


class CreateJobPost(LoginRequiredMixin, generic.CreateView):
    fields = ('company_name', 'title', 'description',
              'experience', 'keyskills', 'location',)

    model = PostJob

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailJobPost(LoginRequiredMixin, generic.DetailView):
    model = PostJob
    template_name = 'postjob/postjob_detail.html'


class ListJobPost(LoginRequiredMixin, generic.ListView):
    model = PostJob

    def get_queryset(self):
        user = self.request.user
        if user.role == 'employer':
            return PostJob.objects.filter(created_by__exact=user.id)
        else:
            applicable_job_list = list()
            active_jobs = PostJob.objects.filter(status__exact=True)
            employee = EmployeeProfile.objects.get(user=user)
            job_applications = JobApplication.objects.filter(user=employee)

            # Loop through all the active jobs
            for current_job in active_jobs:
                # Assume that the User has not applied to the current job.
                has_not_applied = True
                # Loop through all the job applications the current User
                # has applied to.
                for current_application in job_applications:
                    # Check if the current application is for the current job.
                    if current_application.job == current_job:
                        # User has already applied to the current job
                        has_not_applied = False

                # Check if User has not applied for the current job
                if has_not_applied:
                    # Append the current job ID to the Applicable Job List
                    applicable_job_list.append(current_job.id)
            # Return the Queryset
            return PostJob.objects.filter(pk__in=applicable_job_list)


class UpdateJobPost(LoginRequiredMixin, generic.UpdateView):
    fields = ('title', 'description', 'experience', 'keyskills',)
    model = PostJob


class DeactiveJobPost(LoginRequiredMixin, generic.UpdateView):
    redirect_field_name = 'postjob/postjob_list.html'
    fields = ('status',)
    model = PostJob


@login_required(login_url=reverse_lazy('accounts:login'))
def deactivate_job(request, pk):
    post = PostJob.objects.get(id=pk)
    post.status = False
    post.save()
    return redirect('postjob:list')


@login_required(login_url=reverse_lazy('accounts:login'))
def apply_job(request, pk):
    userid = request.user.id
    if request.user.role == 'employee':
        job = PostJob.objects.get(id=pk)
        user = EmployeeProfile.objects.get(user=userid)
        try:
            job_application = JobApplication.objects.get(user=user, job=job)
        except JobApplication.DoesNotExist:
            job_application = False

        if job_application:
            return HttpResponse("You have already applied to this Job")
        else:
            application = JobApplication(job=job, user=user)
            application.save()

    else:
        print("Not Employee")
        return HttpResponse("Register as an Employee to apply for this JOB")
    return HttpResponseRedirect(reverse('postjob:list'))


@login_required(login_url=reverse_lazy('accounts:login'))
def display_job_applications(request, pk):
    applicant_list = list()
    if request.user.role == 'employer':
        job = PostJob.objects.get(id=pk)
        job_title = job.title
        job_applications = JobApplication.objects.filter(job=job).order_by('rank')
        job_skill = job.keyskills
        for application in job_applications:
            employee = User.objects.get(email=application.user)
            applicant = EmployeeProfile.objects.get(user=employee)

            applicant_skill = applicant.keyskills
            similar_skill, match_percent = match_skills(job_skill, applicant_skill)

            app_dict = {'name': employee.first_name + " " + employee.last_name, 'applicant': applicant,
                        'rank': match_percent}
            applicant_list.append(app_dict)

        applicant_list = sorted(applicant_list, key=itemgetter('rank'), reverse=True)
    return render(request, 'postjob/display_applications.html',
                  {'job_title': job_title, 'applicant_list': applicant_list})


def match_skills(job_skill, applicant_skill):
    job_skill = split_list(job_skill)
    applicant_skill = split_list(applicant_skill)
    skill_len = len(job_skill)
    job_skill = convert_lower(job_skill)
    applicant_skill = convert_lower(applicant_skill)
    skills_matched = set(job_skill) & set(applicant_skill)

    match_percent = (len(skills_matched) / skill_len) * 100

    return skills_matched, match_percent

    # Ratio = fuzz.ratio(Str1.lower(),Str2.lower())


def convert_lower(text_list):
    lowercase_list = [x.lower() for x in text_list]
    return lowercase_list


def split_list(text_list):
    text_list = text_list.split(",")
    return text_list
