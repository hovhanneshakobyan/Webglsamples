#!/usr/bin/python
import os
import random
from selenium import webdriver
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path=r'/usr/bin/geckodriver')
driver.get("https://webglsamples.org/aquarium/aquarium.html")
#driver.get('https://webglsamples.org/')
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[1]/section').click()
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
sleep(3)
driver.find_element_by_xpath('//*[@id="setSetting0"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting1"]').click()
print (elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting2"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting3"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting4"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting5"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting6"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting7"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting8"]').click()
print(elem)
sleep(2)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
driver.find_element_by_xpath('//*[@id="setSetting9"]').click()
#os.system("echo elem  >> aaa ")
#list1 = [a,b,c,d,e,f,g,h,l,m]
#random.choice(list1).click()
#elem = driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
#print(elem)
sleep(2)
driver.close()
