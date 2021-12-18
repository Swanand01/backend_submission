from celery import shared_task
from .api_test import get_videos
from .models import Video
from django.utils.dateparse import parse_datetime

from googleapiclient.errors import HttpError

api_keys = ["AIzaSyCBMISH0QZL7xZqGx__gHzpYhFf8-T6XOU"]


@shared_task
def save_new_videos():
    succeeded = False
    for i in range(len(api_keys)):
        try:
            videos = get_videos(api_keys[i])
            succeeded = True
            break
        except HttpError as e:
            if e.status_code == 403 and e.error_details[0]["reason"] == "quotaExceeded":
                print(e.status_code, e.error_details)

    if succeeded:
        for item in videos["items"]:
            yt_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            thumbnail = item["snippet"]["thumbnails"]["high"]["url"]
            pub_date = item["snippet"]["publishedAt"]

            if not Video.objects.filter(yt_id=yt_id).exists():
                video_obj = Video(title=title,
                                  description=description,
                                  thumbnail=thumbnail,
                                  pub_date=parse_datetime(pub_date),
                                  yt_id=yt_id
                                  )
                video_obj.save()
