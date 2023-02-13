
from django.urls import path , include
from . import views
from . import api

app_name = 'jobs'
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    path('api/list', api.joblistapi, name='joblistapi'),
]
