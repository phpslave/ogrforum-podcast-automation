from youtube_api import YouTubeAPI

def upload_to_youtube(video_file, title, description, tags, playlist_id):
    """
    Upload video to YouTube.
    """
    youtube = YouTubeAPI()
    youtube.upload(video_file, title=title, description=description, tags=tags, playlist_id=playlist_id)
