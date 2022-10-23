from fileinput import filename
from sqlite3 import OperationalError
from selenium import webdriver
import requests
import io
from PIL import Image

PATH = "E:\\autoposter insta\\chromedriver.exe"

wd = webdriver.Chrome(PATH)

image_url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"


def download_image(download_path, url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path+file_name
    with open(file_path, "wb") as f:
        image.save(f, "JPEG")
    print("it worked")


download_image("", image_url, "test.jpg")
