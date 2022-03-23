class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt  # yt物件
        self.caption = caption
        self.time = time

    def __str__(self):
        return "<Found(yt=" + str(self.yt) + ")>"

    def __repr__(self):
        content = ":".join([
            "yt=" + str(self.yt),  # 要將yt物件轉換為str,但沒有定義要怎麼轉換所以出現的是位置,去yt.py新增str&repr
            "caption=" + str(self.caption),  # 印出yt物件的簡化版
            "time=" + str(self.time)  # 印出yt物件的簡化版
        ])
        return "<Found(" + content + ")>"
