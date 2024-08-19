import os
import requests
from bs4 import BeautifulSoup

query = input("Keyword: ")
search_url = f"https://imnews.imbc.com/more/search/?search_kwd={query}"

download_folder = f"./{query}"

response = requests.get(search_url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

image_tags = soup.find("div", class_="thumb_type")
lis = image_tags.find_all("li")

downloaded = 0

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for img_tag in lis:
    img_url = img_tag.find("img").get("src")
    img_data = requests.get(f"https:{img_url}").content
    
    downloaded += 1
    image_name = os.path.join(download_folder, f"image_{downloaded}.jpg")

    with open(image_name, "wb") as img_file:
        img_file.write(img_data)

print(f"Downloaded {downloaded} images to {download_folder}")
