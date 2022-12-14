import csv
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
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome() #웹 드라이버가 저장되는 경로입니다.
# driver.get('http://www.poemlove.co.kr')

# CSV 생성
filename = "poem_plus_5900.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline="")
writer_csv = csv.writer(f)

title = (["제목", "시인", "시"])
writer_csv.writerow(title)

data = []

# 100개의 시를 크롤링하여 본문과 제목 시인으로 나누기

for i in range(5900,6000) :
    url = "http://www.poemlove.co.kr/bbs/board.php?bo_table=tb01&page={}".format(i)
    driver.get(url)
    time.sleep(1)

    for num in range(1,26):
            poem = driver.find_element_by_css_selector("#fboardlist > div.list-board > ul > li:nth-child({}) > div.wr-subject > a".format(num)).text
            driver.find_element_by_css_selector("#fboardlist > div.list-board > ul > li:nth-child({}) > div.wr-subject > a".format(num)).send_keys(Keys.ENTER)
            time.sleep(1)
            try :
                poem_list = []
                
                if '-' in poem :
                    poem = poem.split(" - ")
                    title = poem[0]
                else :
                    title = poem

                author = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[10]/section[1]/article/div[2]/div/strong[1]').text

                text = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/div[10]/section/article/div[3]/div[2]')

                for ele in text :
                    text = ele.get_attribute("innerText")
            
                text = text.splitlines(True) 
                text = " ".join(text) 
                
                poem_list.append(title)
                poem_list.append(author)
                poem_list.append(text)

                writer_csv.writerow(poem_list)
                # data.append(poem_list)
            
            except :
                pass

            driver.back()
            time.sleep(1)
                       
      
driver.close()
