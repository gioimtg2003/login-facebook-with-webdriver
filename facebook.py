import random
import time
from selenium import webdriver
from threading import Thread
from selenium.webdriver.common.keys import Keys
import pickle

file = open("account.txt")


def func(number):
    driver = webdriver.Chrome()
    x = number*250
    y = 0
    driver.set_window_rect(x, y, width=200, height=600)

    Options = webdriver.ChromeOptions()

   
    driver.get(url)
    # driver.set_window_size(200,600)
    # tk = file.readline()
    # mk = file.readline()

    # driver.find_element_by_id("email").send_keys(tk)
    # time.sleep(2)
    # driver.find_element_by_id("pass").send_keys(mk)
    # time.sleep(2)
    # driver.find_element_by_id("pass").send_keys(Keys.ENTER)
    if (number == 0):
        filee = "account0.pkl"
    if (number == 1):
        filee = "account0.pkl"
    cookies = pickle.load(open(filee, "rb"))
    if (number == 2):
        filee = "account0.pkl"
    if (number == 3):
        filee = "account0.pkl"
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(2)
    for j in range(100):
        driver.execute_script('window.scrollBy(0,200)')
        time.sleep(2)
    time.sleep(10000)
   


url = 'https://www.facebook.com/'

soluong = int(input("Nhập số nick chạy: "))



threads = []

for number in range(soluong):
    
    t = Thread(target=func, args={number},)

    time.sleep(1)
    t.start()


for t in threads:
    t.join()
