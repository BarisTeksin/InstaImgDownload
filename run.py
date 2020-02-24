import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import wget
import sys

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
username = input('İnstagram Kullanıcı Adınız : ')
passwd = input('İnstagram Şifreniz : ')
url = input('İnstagram profil linki : ')
foto_sayisi = int(input('Fotoğraf sayısı : '))
if foto_sayisi<=24:
    page = 1
else:
    page = int((foto_sayisi - 24) / 12 + 2)

driver_path = "C:\\Users\\bteks\\Desktop\\chromedriver.exe" # Buraya chrome driver adresiniz \\ ile yazılacak.
driver = webdriver.Chrome(executable_path=driver_path)
driver.set_page_load_timeout(25)
driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
driver.implicitly_wait(30)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(passwd)
driver.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(5)
driver.get(url)
driver.implicitly_wait(30)

img_url = []
for x in range(page):
    body = driver.find_element_by_tag_name('body').get_attribute('innerHTML')
    soup = BeautifulSoup(body,'html.parser')
    resim_ana_urller = soup.find('article').findAll('a',href=True)
    for resim in resim_ana_urller:
        if resim.get('href') in img_url:
            continue
        else:
            img_url.append(resim.get('href'))
    ActionChains(driver).key_down(Keys.END).key_up(Keys.END).perform()
    time.sleep(1)
print(img_url)
driver.quit()

for resim_ana_url in img_url:
    r = requests.get('https://www.instagram.com' + resim_ana_url,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')
    resim_linki = soup.find('meta',attrs={'property':'og:image'}).get('content')
    wget.download(resim_linki)