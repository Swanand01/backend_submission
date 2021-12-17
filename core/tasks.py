from celery import shared_task
from .api_test import get_videos
from .models import Video
from django.utils.dateparse import parse_datetime


@shared_task
def save_new_videos():
    videos = get_videos()

    for item in videos["items"]:
        yt_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        thumbnail = item["snippet"]["thumbnails"]["default"]["url"]
        pub_date = item["snippet"]["publishedAt"]

        print("Title:", title)
        print("description:", description)
        print("pub_date:", pub_date)
        print("thumbnail:", thumbnail)
        print("yt_id:", yt_id, "\n")

        if not Video.objects.filter(yt_id=yt_id).exists():
            video_obj = Video(title=title,
                              description=description,
                              thumbnail=thumbnail,
                              pub_date=parse_datetime(pub_date),
                              yt_id=yt_id
                              )
            video_obj.save()
