from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        "channel_id": channel_id
    }
    steps = [
        GetVideoList()
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
