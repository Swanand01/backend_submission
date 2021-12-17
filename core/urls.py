from django.urls import path
from . import views

urlpatterns = [
    path('api/videos/', views.video_endpoint, name="video_endpoint"),
    path('dashboard/', views.dashboard, name='dashboard')
]
