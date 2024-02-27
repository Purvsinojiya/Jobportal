from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  # Add this import
from .models import Job
from .serializers import JobSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Count, Avg, Min, Max
from .filter import JobFilter
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def getAllJobs(request):
    filterset = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    count = filterset.qs.count()
    
    # Pagination
    resPerPage = 2
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = JobSerializer(queryset, many=True)  # Serialize the paginated queryset
    return paginator.get_paginated_response({
        "count": count,
        "resPerPage": resPerPage,
        "jobs": serializer.data
    })

@api_view(['GET'])
def getJob(request,pk):
    job = Job.objects.filter(id=pk)
    serializer = JobSerializer(job, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def newJob(request):
    data = request.data
    job=job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateJob(request,pk):
    job = Job.objects.filter(id=pk)
    
    job.title=request.data['title']
    job.description=request.data['description']
    job.email=request.data['email']
    job.address=request.data['address']
    job.jobType=request.data['jobType']
    job.education=request.data['education']
    job.industry=request.data['industry'] 
    job.experience=request.data['experience'] 
    job.salary=request.data['salary'] 
    job.positions=request.data['positions']
    job.company=request.data['company']
    job.save()
   
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteJob(request,pk):
   job = Job.objects.get(id=pk) 
   job.delete()
   return Response({'message':'Job is deleted'},status=status.HTTP_200_OK)

@api_view(['GET'])
def gettopics(request, topic):
    args = {'title__icontains': topic}
    jobs = Job.objects.filter(**args)
    
    if len(jobs) == 0:
        return Response({'message': f'No topics available {topic}'})
    
    stats = jobs.aggregate(
        total_jobs=Count('title'),
        avg_positions=Avg('positions'),
        avg_salary=Avg('salary'),
        min_salary=Min('salary'),
        max_salary=Max('salary')
    )
    return Response(stats)