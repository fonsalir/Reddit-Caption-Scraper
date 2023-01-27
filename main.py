from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

#how many reddit titles will be scrapped
requested_amount = input("how many?: ")
try:
    int_requested_amount = int(requested_amount)
except ValueError:
    sys.exit("Invalid")

print(int_requested_amount)

#gets the path of my chrome driver
service = Service(executable_path="C:\Program Files (x86)\chromedriver")
driver = webdriver.Chrome(service=service)

SITE="https://www.reddit.com/"
driver.get(SITE)

html = driver.find_element(By.TAG_NAME,'html')
h3tags = driver.find_elements(By.XPATH, "//h3")


captions = set()
loop = True
while loop:
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    h3tags = driver.find_elements(By.XPATH, "//h3")
    for tag in h3tags:
        captions.add(tag.text)
        if len(captions) >= int_requested_amount:
            loop = False

captions = list(captions)
if "" in captions:
    captions.remove("")
if len(captions) >=  int_requested_amount:
    for caption in range(int_requested_amount):
        print(captions[caption])
else:
    for caption in captions:
        print(caption)