import requests
import os
from bs4 import BeautifulSoup


URL = "https://yandex.ru/images/"
HEADERS={"User-Agent": "Mozilla/5.0"}

def get_image(url, filename, index):
 if not os.path.isdir(filename):
  os.mkdir(filename)
 response = requests.get(f"https:{url}", HEADERS)
 saver = open(os.path.join(f"{filename}/{str(index).zfill(4)}.jpg"), "wb")
 saver.write(response.content)
 saver.close()

def download_img(path, query):
 os.chdir(path)
 if not os.path.isdir("dataset"):
  os.mkdir("dataset")
os.chdir("dataset")
