
from selenium import webdriver   #引用selenium中所有的方法 from selenium import *
browser=webdriver.Chrome('/Users/wuxiaomeng/Documents/selenium/chromedriver')
browser.get('http://www.kugou.com/')

input1=browser.find_element_by_css_selector('[type="text"]').send_keys('体面')
button1=browser.find_element_by_css_selector('.searh_btn').click()
checkbox1=browser.find_element_by_css_selector('.search_icon.checkall').click()
button2=browser.find_element_by_css_selector('.play_all').click()



