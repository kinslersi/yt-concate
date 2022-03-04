from abc import ABC  # 抽象類別helper class
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):  # 繼承build-in的Exception，在過程中任何一個時間停止會觸發stepexception，然後用try except來捕捉錯誤
    pass
