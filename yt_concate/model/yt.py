import os
from yt_concate.setting import CAPTIONS_DIR
from yt_concate.setting import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    def __str__(self):
        return "<YT(" + str(self.id) + ")>"

    def __repr__(self):
        content = ":".join([
            "id=" + str(self.id),
            "caption_filepath=" + str(self.caption_filepath),
            "video_filepath=" + str(self.video_filepath)
        ])
        return "<YT(" + content + ")>"

    @staticmethod
    def get_video_id_from_url(url):
        return url.split("watch?v=")[1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + ".txt")

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + ".mp4")
