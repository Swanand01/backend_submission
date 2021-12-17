from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.TextField(default="")
    description = models.TextField(default="")
    thumbnail = models.TextField(default="")
    pub_date = models.DateTimeField()
    yt_id = models.TextField(default="")

    def __str__(self):
        return self.title
