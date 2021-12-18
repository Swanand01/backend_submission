from django.shortcuts import render
from .models import Video

from rest_framework.decorators import api_view
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(["GET"])
def video_endpoint(request):
    """
    This is the API endpoint that serves all the stored videos in a paginated format, in the descending order of published datetime.
    
    url: /api/videos
    """
    videos = Video.objects.all().order_by("-pub_date")

    paginator = PageNumberPagination()
    paginator.page_size = 2 #Sets the number of videos per page.

    result_page = paginator.paginate_queryset(videos, request)
    serializer = VideoSerializer(result_page, many=True) #Serialize the paginated queryset
    return paginator.get_paginated_response(serializer.data)


def dashboard(request):
    """
    This is the view for the dashboard. Lists the stored videos in a card view, in descending order of their published datetime. Also has a search bar to search for videos.

    url: /dashboard
    """
    videos = Video.objects.all().order_by("-pub_date")

    if request.GET.get("search"):
        keyword = request.GET.get("search")
        videos = Video.objects.filter(
            title__icontains=keyword).order_by("-pub_date")

    context = {
        "videos": videos
    }
    return render(request, "dashboard.html", context)
