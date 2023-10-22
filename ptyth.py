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

def download_image(path, query):
 os.chdir(path)
 if not os.path.isdir("dataset"):
  os.mkdir("dataset")
os.chdir("dataset")

count = 0
page = 0

while count< 1000:
 query_1= query.replace("", "%20")
 url=f'{URL}search?p={page}&text={query}'
 print(f"Fetching URL: {url}")

 response=requests.get(url,headers=HEADERS)

 soup=BeautifulSoup(response.text, "html.parser")
 image_link= soup.findAll('img', class_='serp-item__thumb justifier__thumb')
 if not image_link:
  print("No correct images found on this page")
  break
 
 for image in image_link:
  if count==1000:
   url=image.get("src")
   if url and not url.startswith("data:"):
    get_image(url, query, count)
    count+=1
    print(count) 
    page +=1

    
