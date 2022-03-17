import time

from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownLoadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print("downloading caption for url")  # 現在執行哪一個程式
            if utils.caption_file_exist(url):  # 如果程式存在就略過
                print("found existing file")
                continue
            try:
                srt = YouTubeTranscriptApi.get_transcript(utils.get_video_id_from_url(url))
                with open(utils.get_caption_filepath(url), "w") as f:
                    for i in str(srt):
                        f.write(i)

            except Exception:
                print('error when downloading caption for', url)
                continue
        end = time.time()
        print("took", end - start, "seconds")