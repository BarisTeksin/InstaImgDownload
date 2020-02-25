import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import wget
import sys

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

driver_path = "C:\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.set_page_load_timeout(10)
driver.maximize_window()

def login(user_username,user_password):
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    driver.implicitly_wait(10)
    driver.find_element_by_name('username').send_keys(user_username)
    driver.find_element_by_name('password').send_keys(user_password)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    time.sleep(5)

def user_photo_count(username):
    try:
        r = requests.get('https://www.instagram.com/'+username,headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        photo_count = int(soup.find('meta',attrs={'property':'og:description'}).get('content').split('Following, ')[1].split(' ')[0].replace(',',''))
    except:
        print('Profile not found.')
        sys.exit()
    if photo_count<=24:
        page = 1
    else:
        page = int((photo_count - 24) / 12 + 3)



def DownloadProfilePhotos(username):
    page = user_photo_count(username)
    driver.get('https://www.instagram.com/'+username)
    driver.implicitly_wait(10)
    time.sleep(3)

    img_url = []
    for x in range(page):
        body = driver.find_element_by_tag_name('body').get_attribute('innerHTML')
        soup = BeautifulSoup(body,'html.parser')
        photo_main_urls = soup.find('article').findAll('a',href=True)
        for photo in photo_main_urls:
            if photo.get('href') in img_url:
                continue
            else:
                img_url.append(photo.get('href'))
        ActionChains(driver).key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(3)
    driver.quit()

    for photo_main_url in img_url:
        r = requests.get('https://www.instagram.com' + photo_main_url,headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        photo_link = soup.find('meta',attrs={'property':'og:image'}).get('content')
        wget.download(photo_link)

def DownloadTagPhotos(username):
    page = user_photo_count(username)
    driver.get('https://www.instagram.com/'+username+'/tagged/')
    driver.implicitly_wait(10)
    time.sleep(3)

    img_url = []
    for x in range(page):
        body = driver.find_element_by_tag_name('body').get_attribute('innerHTML')
        soup = BeautifulSoup(body,'html.parser')
        photo_main_urls = soup.find('article').findAll('a',href=True)
        for photo in photo_main_urls:
            if photo.get('href') in img_url:
                continue
            else:
                img_url.append(photo.get('href'))
        ActionChains(driver).key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(3)
    driver.quit()

    for photo_main_url in img_url:
        r = requests.get('https://www.instagram.com' + photo_main_url,headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        photo_link = soup.find('meta',attrs={'property':'og:image'}).get('content')
        wget.download(photo_link)
