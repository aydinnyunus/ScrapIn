import soup as soup
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

link = "https://www.linkedin.com/in/yunus-ayd%C4%B1n-b9b01a18a/"

browser = webdriver.Chrome('C:/Users/aydin/Desktop/chromedriver.exe')
browser.get('https://www.linkedin.com/login')
file = open('sample.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

browser.get(link)

SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(3):
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

name_div = soup.find('div', {'class': 'flex-1 mr5'})
name_loc = name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()
print(name)