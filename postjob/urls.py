from django.urls import path

from postjob import views


app_name = 'postjob'


urlpatterns = [
    path('create/',views.CreateJobPost.as_view(),name='create'),
    path('list/',views.ListJobPost.as_view(),name='list'),
    path('<int:pk>/',views.DetailJobPost.as_view(),name='detail'),
    path('update/<int:pk>/',views.UpdateJobPost.as_view(),name='update'),
    #path('deactivate/<int:pk>/',views.DeactiveJobPost.as_view(),name='deactivate'),
    path('deactivate/<int:pk>/', views.deactivate_job, name='deactivate'),
    path('applyjob/<int:pk>/',views.apply_job,name='applyjob'),
    path('displayjobapplications/<int:pk>/',views.display_job_applications,name='jobapplications'),
]
