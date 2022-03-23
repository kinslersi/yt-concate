import time

from youtube_transcript_api import YouTubeTranscriptApi
from yt_concate.pipeline.steps.step import Step


class DownLoadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:  # data已經變成裝載著很多yt物件
            print("downloading caption for url", yt.id)  # 現在執行哪一個程式
            if utils.caption_file_exist(yt):  # 如果程式存在就略過
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
        return data  # 接收data傳進來,沒有像get_video_list取得資料,就處理好再傳data出去
