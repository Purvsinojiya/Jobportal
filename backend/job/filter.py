from django_filters import rest_framework as filters
from .models import Job

class JobFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name='title',lookup_expr='icontains')
    location = filters.CharFilter(field_name='address',lookup_expr='icontains')
    min_salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    
    class Meta:
        model = Job
        fields = ('keyword','education', 'jobType', 'experience')
