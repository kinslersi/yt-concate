import time

from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownLoadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print("downloading caption for url", yt.id)
            if utils.caption_file_exist(yt):
                print("found existing file")
                continue
            try:
                srt = YouTubeTranscriptApi.get_transcript(yt.url)
                with open(yt.caption_filepath, "w") as f:
                    for i in str(srt):
                        f.write(i)

            except Exception:
                print('error when downloading caption for', yt.url)
                continue
        end = time.time()
        print("took", end - start, "seconds")
        return data
