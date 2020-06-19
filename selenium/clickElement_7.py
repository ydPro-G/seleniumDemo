# 点击元素
# 调用元素WebElement对象的click方法
# 点击的是该元素点的中心位置
# .click()
from selenium import webdriver

clicks = webdriver.Chrome()

clicks.get('https://www.baidu.com')

clicks.find_element_by_id('kw').send_keys('最新消息') # 指定输入框，发送键（send_keys）

clicks.find_element_by_id('su').click() # 指定元素，点击（click）

from time import sleep # 等待时间2秒
sleep(2)




# 输入框
# 调用元素WebElement对象的send.keys方法
# 实例.元素.send_keys('消息')







# 获取元素文本内容 ，通过————.text属性
# 变量 = 实例.方法（元素）
# print(变量.text)