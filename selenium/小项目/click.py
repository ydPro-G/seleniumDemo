from selenium import webdriver
from time import sleep

wb = webdriver.Chrome()

wb.get('https://cy4.youwuu.com/login/index/index.html')

name = wb.find_element_by_id('user_login_username')
name.send_keys('CSHM001')

pw = wb.find_element_by_id('user_login_password')
pw.send_keys('password')

ck = wb.find_element_by_xpath('//div[@class="layui-form-item"]/button')

sleep(3)
ck.click()
sleep(10)
ms = wb.find_element_by_xpath('//div[@class="layui-push-left layui-form"]/button')
ms.click()

