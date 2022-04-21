from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random
import math

messagesList = list()

with open ('messages.txt','r',encoding=('utf-8')) as messages:
    text = messages.read()
    messagesList = text.split('\n')

print(messagesList)

def start():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input("QR girip ekranı açtıktan sonra enterla")
    
    while True:
        time.sleep(0.5)
        message_area = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        wp_source = driver.page_source
        soup = bs(wp_source,'lxml')

        screen_messages = soup.find_all('div',{'class':'copyable-text'})
        try:
            command = str(screen_messages[-2].span.text).split(" ")
            if command[0] == 'exec':
                try:
                    command = command[1:]
                    st = ' '.join(command)
                    print(st)
                    val = eval(st)
                    message_area.click()
                    message_area.send_keys(str(val))
                    message_area.send_keys(Keys().ENTER)
                except Exception as ex:
                    print(f'Exception "{ex}"')
        except Exception as ex:
            print(f'Exception "{ex}"')
start()