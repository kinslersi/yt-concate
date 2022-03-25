import math

from moviepy.editor import VideoFileClip, concatenate_videoclips
from .step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_time(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            # if len(clips) >= inputs["limit"]  # 防止記憶體爆掉
            #     break
        final_clip = concatenate_videoclips(clips)  # 清單中累積到20才組合起來
        output_file = utils.output_filepath(inputs["channel_id"], inputs["search_word"])
        final_clip.write_videofile(output_file, audio_codec='aac')   # 有bug,增加聲音

    def parse_time(self, captions_time):
        a, b = captions_time.split("-->")
        start = eval(a)
        end = start + eval(b)
        return self.calculate_time(start), self.calculate_time(end)

    def calculate_time(self, time):
        if time >= 3600:
            hour = math.floor(time / 3600)
            minute = math.floor((time - 3600 * hour) / 60)
            second = (time - 3600 * hour) % 60
            return hour, minute, second
        else:
            minute = math.floor(time / 60)
            second = time % 60
            return 0, minute, second  # return 出來會是tuple
