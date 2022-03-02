import os
from dotenv import load_dotenv  # dotenv套件的功用是讓環境變數存在檔案，然後在把檔案裡的東西丟回環境變數，彷彿好像存在真正的環境變數裡，所以真正讀取的方法還是一樣的

load_dotenv()  # take environment variables from .env.
API_KEY = os.environ["api_key"]  # 從環境變數中把api_key讀取出來