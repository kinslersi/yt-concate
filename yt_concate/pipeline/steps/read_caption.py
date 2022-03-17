import os
import ast
from pprint import pprint

from .step import Step
from yt_concate.setting import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), "r") as f:
                data_file = ast.literal_eval(f.read())
                for line in data_file:
                    caption = line['text']
                    time = str(line["start"]) + "-->" + str(line["duration"])
                    captions[caption] = time
                    data[caption_file] = captions
        pprint(data)
        return data
