# 调用库中模块
from selenium import webdriver

# 创建webdriver对象，指明使用的chrome驱动
test = webdriver.Chrome()

# 调用对象的的get方法，打开指定网址
test.get("https://baidu.com")

# 根据id选择元素，返回的是该元素对应的web元素对象
element = test.find_element_by_id('kw').send_keys('中印边境冲突')

element = test.find_element_by_id('kw').clear()




