import csv
from pdb import post_mortem
import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import warnings
import bs4
import pandas as pd
import numpy as np
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

warnings.filterwarnings('ignore')

option = Options()

# 알림창 끄기
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})


driver = webdriver.Chrome() #웹 드라이버가 저장되는 경로입니다.
driver.implicitly_wait(3)
driver.get('http://raincat.com/?_filter=search&act=&vid=&mid=poem&category=&search_keyword=%EB%B9%84%EA%B3%A0%EC%96%91%EC%9D%B4&search_target=nick_name')

# CSV 생성
filename = "poem.csv"
f = open(filename, "w",encoding = "utf-8-sig",newline="")
writer_csv = csv.writer(f)

title = (["제목", "시인", "시"])
writer_csv.writerow(title)



total_page = 145


data = []
# 100개의 시를 크롤링하여 본문과 제목 시인으로 나누기

for i in range(1,total_page+1) :
    url = "http://raincat.com/index.php?_filter=search&mid=poem&search_keyword=%EB%B9%84%EA%B3%A0%EC%96%91%EC%9D%B4&search_target=nick_name&page={}".format(i)
    driver.get(url)
   
        
    for num in range(1,51):
            poem = driver.find_element_by_css_selector(f'#bd_1651_0 > div.bd_lst_wrp > table > tbody > tr:nth-child({num}) > td.title > a').text
            driver.find_element_by_xpath(f'//*[@id="bd_1651_0"]/div[2]/table/tbody/tr[{num}]/td[2]/a').click()
            
            try :
                poem_list = []

                poem = poem.split(" - ")
                title = poem[0]
                author = poem[1]

                text = driver.find_elements_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div[2]/article/div')
                for ele in text :
                    text = ele.get_attribute("innerText")
            
                text = text.splitlines(True) 
                del text[0:3]
                text = " ".join(text) 
        
                poem_list.append(title)
                poem_list.append(author)
                poem_list.append(text)
            except :
                pass

            driver.back()
            writer_csv.writerow(poem_list)

            data.append(poem_list)           
      
driver.close()
