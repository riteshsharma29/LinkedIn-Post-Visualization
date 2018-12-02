#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
import sys
import unittest
import os
import getpass
import time
import pyautogui

'''
mypost id's - 6471757516186456064, 6465234913842032640, 6465122615416717312, 
open issues
ID 6468885395999424512 - Tesseract not extracting location text with numbers due to which pie chart is not generated properly
'''


userid = 'ritesh.sharma29@gmail.com'
password = getpass.getpass('Enter your password:')
#update your postid
post_id = sys.argv[1]

driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'drivers\\chromedriver.exe'))   
driver.get("https://www.linkedin.com")

username = driver.find_element_by_id("login-email")
username.send_keys(userid)

#Provide password
passwd  = driver.find_element_by_id("login-password")
passwd.send_keys(password)

driver.find_element_by_id('login-submit').click()
driver.implicitly_wait(10)

#Load the post on the browser and Maximize the Post image with pyautogui

post_pg = driver.get("https://www.linkedin.com/in/ritesh-sharma29/detail/recent-activity/shares/ca/share-analytics/urn:li:activity:" + str(post_id) + "/")
driver.maximize_window()
time.sleep(5)
pyautogui.press("tab")
time.sleep(3)
pyautogui.press("tab")
time.sleep(3)
pyautogui.press("tab")
time.sleep(3)
pyautogui.press("tab")
time.sleep(3)
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("down")
time.sleep(3)

#Take post screenshot and close the browser
driver.save_screenshot('screenshot.png')
driver.close()

##################################################################################################################################################


os.system('mkdir CROP')
#Call crop.py to crop image
os.system('python crop.py')