from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('<int:year>/', views.get_video_by_year, name="video_by_year"),
    path('videos/', views.get_videos, name="get_videos")
]