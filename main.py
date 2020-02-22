from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

text_file = open("output.txt", "w")
link = "https://www.linkedin.com/in/yunus-ayd%C4%B1n-b9b01a18a/"

browser = webdriver.Chrome('/home/aydinnyunus/Downloads/chromedriver')
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


loc = name_loc[1].find('li').get_text().strip()


profile_title = name_div.find('h2').get_text().strip()


connection = name_loc[1].find_all('li')
connection = connection[1].get_text().strip()


info = []

exp_section = exp_section.find('ul')
li_tags = exp_section.find('div')
a_tags = li_tags.find('a')

job_title = a_tags.find('h3').get_text().strip()

company_name = a_tags.find_all('p')[1].get_text().strip()

joining_date = a_tags.find_all('h4')[0].find_all('span')[1].get_text().strip()

exp = a_tags.find_all('h4')[1].find_all('span')[1].get_text().strip()

edu_section = soup.find('section', {'id': 'education-section'}).find('ul')
college_name = edu_section.find('h3').get_text().strip()
degree_name = edu_section.find('p', {'class': 'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
stream = edu_section.find('p', {'class': 'pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
degree_year = edu_section.find('p', {'class': 'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[1].get_text().strip()

print("Informations are writing in text file")

info.append(link)
info.append(name)
info.append(profile_title)
info.append(loc)
info.append(connection)

info.append(company_name)
info.append(job_title)
info.append(joining_date)
info.append(exp)

info.append(college_name)
info.append(degree_name)
info.append(stream)
info.append(degree_year)

text_file.write(info)
text_file.close()

