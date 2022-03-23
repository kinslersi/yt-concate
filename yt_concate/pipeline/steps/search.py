from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs["search_word"]
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:  # 跳過沒有字幕的yt物件
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]  # 當初設定captions[time:caption]
                    f = Found(yt, caption, time)  # 創作出實例
                    found.append(f)
        print(found)
        return found  # data進來,但重新創造新的一份資料集
