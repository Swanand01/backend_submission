from django.shortcuts import render
from .models import Video

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

# Change to JSONResponse later
@api_view(["GET"])
def video_endpoint(request):
    videos = Video.objects.all().order_by("-pub_date")

    paginator = PageNumberPagination()
    paginator.page_size = 2

    result_page = paginator.paginate_queryset(videos, request)
    serializer = VideoSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


def dashboard(request):
    videos = Video.objects.all().order_by("-pub_date")
    context = {
        "videos": videos
    }
    return render(request, "dashboard.html", context)
