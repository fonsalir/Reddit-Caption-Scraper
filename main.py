from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#from colorama import Fore, Back, Style

#gets the path of my chrome driver
service = Service(executable_path="C:\Program Files (x86)\chromedriver")
driver = webdriver.Chrome(service=service)

SITE="https://www.reddit.com/"
driver.get(SITE)

html = driver.find_element(By.TAG_NAME,'html')
h3tags = driver.find_elements(By.XPATH, "//h3")

captions = []
while True:
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    h3tags = driver.find_elements(By.XPATH, "//h3")
    captions = {"",}
    for tag in h3tags:
        captions.add(tag.text)
    if len(captions) >= 10:
        break

for caption in captions:
    print(caption)