# 为什么要设置等待时长？
# 因为我们代码执行速度比服务器响应速度快，所以一些高响应的结果时间不到获取不到

# 时长方法1 sleep 等待2秒
# for time import sleep
# sleep(2) # 等待时长两秒

# 时长方法2  implicitly_wait 等待2秒
# 实例. implicitly_wait(2)  # 周期性（半秒）寻找数据，找到返回，最大时长为2秒






from selenium import webdriver

wd = webdriver.Chrome()

# webdriver对象的implicitily_wait(隐式等待)方法，每半秒重新寻找该元素
wd.implicitly_wait(10)# 接受一个参数指定最大等待时长

wd.get('https://www.baidu.com')

elements = wd.find_element_by_id('kw').send_keys('中美谈判')
wd.find_element_by_id('su').click() # 单击元素
element = wd.find_element_by_id('1') # 寻找kw里的id为1的元素

print(element.text)
