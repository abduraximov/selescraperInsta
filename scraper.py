from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

load_dotenv()
username = os.environ['username']
password = os.environ['password']


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("http://instagram.com")
    time.sleep(10)
    name = driver.find_element(by=By.NAME, value="username")
    passw = driver.find_element(by=By.NAME, value="password")
    time.sleep(2)
    name.send_keys(username)
    passw.send_keys(password)
    submit = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
    submit.click()
    time.sleep(20)

    # search profile
    driver.get("http://instagram.com/abdurakhimov01/")
    time.sleep(20)
    image_link = driver.find_element(by=By.CSS_SELECTOR, value="a[role='link']")
    print(image_link.get_attribute("href"))
    time.sleep(15)

    anchors = driver.find_elements(by=By.TAG_NAME, value="a")
    anchors = [a.get_attribute('href') for a in anchors]

    for i, a in enumerate(anchors):
        if str(a).startswith("https://www.instagram.com/p/"):
            print(a)
            post_url = a.split("/p/")[-1].split("/")[0]
            img_url = f"https://www.instagram.com/p/{post_url}/media/?size=l"
            urllib.request.urlretrieve(img_url, os.path.join("folder", f"{i}.jpg"))
            # if not InstaPost.objects.filter(url=a).exists():
            #     obj = InstaPost.objects.create(url=a, post=f"instagram/{i}.jpg")
            #     obj.save()

    driver.quit()


test_eight_components()

