import django_filters
from job.models import Job

class JobFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'description', 'salary', 'category']