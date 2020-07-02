from selenium import webdriver
from time import sleep

wb = webdriver.Chrome()

wb.get('https://cy4.youwuu.com/login/index/index')



username = wb.find_element_by_id('user_login_username')
username.send_keys('username')

userpassword = wb.find_element_by_id('user_login_password')
userpassword.send_keys('password')

cilck = wb.find_element_by_css_selector(
    '.layui-form-item > button'
)
sleep(5) 
cilck.click()
sleep(20) # 点击登录按钮后等待20秒


filename = 'gailan.txt'

with open(filename,'w',encoding='utf-8') as file_object:
    elements = wb.find_element_by_css_selector(
        'ul >li > span'
    )
    file_object.write(elements.text)

