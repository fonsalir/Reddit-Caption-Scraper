from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import csv
from colorama import Fore


#how many reddit titles will be scrapped
requested_amount = input("how many?: ")
try:
    int_requested_amount = int(requested_amount)
except ValueError:
    sys.exit("Invalid")


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
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1.5)
    h3tags = driver.find_elements(By.XPATH, "//h3")
    for tag in h3tags:
        if tag.text == "":
            pass
        else:
            captions.add(tag.text)
        if len(captions) >= int_requested_amount:
            loop = False
    
    print(f"{Fore.GREEN + str(len(captions))} captions")

captions = list(captions)



if len(captions) != int_requested_amount:
    captions_dict = {captions[caption]:"caption" for caption in range(int_requested_amount)}
else:
    captions_dict = {caption:"caption" for caption in captions}

with open("captions.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for caption in captions_dict:
        writer.writerow({caption})
    