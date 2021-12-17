from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Video
# Create your views here.


def dashboard(request):
    videos = Video.objects.all().order_by("-pub_date")
    context = {
        "videos": videos
    }
    return render(request, "dashboard.html", context)
