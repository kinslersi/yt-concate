import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["api_key"]

DOWNLOADS_DIR = "downloads"
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, "videos")  # downloads/videos
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, "captions")  # downloads/captions
