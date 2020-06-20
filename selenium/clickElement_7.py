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

clicks.quit() # 退出






# 输入框
# 调用元素WebElement对象的send.keys方法
# 实例.元素.send_keys('消息')









# 获取元素文本内容 ，通过————.text属性
# 变量 = 实例.方法（元素）
# print(变量.text)








# 获取元素属性的值
# 获取元素属性class的值，可以使用element.get_attribute('class')


from selenium import webdriver

wd = webdriver.Chrome()

wd.get('http://cdn1.python3.vip/files/selenium/test3.html')

element = wd.find_element_by_id('input1')
print(element.get_attribute('value'))  #获取元素的属性值

wd.quit()








# 获取整个元素对应的HTML
# 要获取整个元素对应的html文本内容可以使用element.get_attribute('outerHTML')
# 要获取某个元素对应内部的HTML文本内容，可以使用element.attribute('innerHTML')
print(element.get_attribute('outerHTML'))







# 获取元素文本内容2
# element.get_attribute('innerText')