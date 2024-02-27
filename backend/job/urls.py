from django.urls import path
from . import views


urlpatterns = [
    path('jobs/',views.getAllJobs,name='jobs'),
    path('jobs/new',views.getAllJobs,name='new_job'),
    path('jobs/<str:pk>/',views.getJob,name='job'),
    path('jobs/<str:pk>/update/',views.updateJob,name='update_job'),
    path('jobs/<str:pk>/delete/',views.deleteJob,name='delete_job'),
    path('stats/<str:topic>/',views.gettopics,name='get_topic_stats'),
]