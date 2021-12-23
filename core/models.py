from django.db import models


class Video(models.Model):
    """
    Database model for a YouTube video.\n
    Attributes:\n
    title: Title of the video
    description: Description of the video
    thumbnail: URL of the video's thumbnail
    pub_date: Datetime when the video was published
    yt_id: Unique ID
    """
    title = models.TextField(default="")
    description = models.TextField(default="")
    thumbnail = models.TextField(default="")
    pub_date = models.DateTimeField()
    yt_id = models.TextField(default="")

    def __str__(self):
        return self.title
