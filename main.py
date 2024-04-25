from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime


def check_whatsapp_status():
    with webdriver.Chrome() as driver:
        driver.implicitly_wait(5)
        driver.get("https://web.whatsapp.com/")
        input("Please select user and hit enter to continue...")
        user_is_online = False
        while True:
            try:
                whatsapp_source = driver.page_source

                soup = BeautifulSoup(whatsapp_source, 'lxml')
                online_tag = soup.find("div", {"class": "x78zum5 x1cy8zhl xisnujt x1nxh6w3 xcgms0a x16cd2qt"})
                online_status = online_tag.span["title"].strip()

                print(online_status)

                if online_status is not None and user_is_online is False and online_status in ["online"]:
                    user_is_online = True
                    print("User is online now")
                else:
                    user_is_online = False
                    print("User is offline still")

            except:
                print("Status cant captured")
                user_is_online = False

            finally:
                time.sleep(3)


check_whatsapp_status()
