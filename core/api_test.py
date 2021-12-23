# -*- coding: utf-8 -*-
import os
import googleapiclient.discovery


def get_videos(api_key):
    """
    Fetches videos from YouTube, by calling YouTube Data V3 API.

    args: api_key: YouTube API key.\n
    returns: response: collection of search results that match the query parameters specified.
    """

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Specify query parameters
    request = youtube.search().list(
        part="snippet",
        order="date",
        q="cricket",
        type="video",
        publishedAfter="2020-01-01T00:00:00Z"
    )

    response = request.execute()
    return response
