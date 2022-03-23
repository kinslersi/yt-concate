import ast

from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exist(yt):  # 如果下載的文檔沒有的話就會continue到下一個data
                continue

            with open(yt.caption_filepath, "r") as f:  # 文檔存在就會讀入
                captions = {}
                data_file = ast.literal_eval(f.read())
                for line in data_file:
                    caption = line['text']
                    time = str(line["start"]) + "-->" + str(line["duration"])
                    captions[caption] = time
            yt.captions = captions
        return data  # 接收data傳進來,沒有像get_video_list取得資料,就處理好再傳data出去
