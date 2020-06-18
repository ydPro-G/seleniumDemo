# class 属性标志着元素类型
from selenium import webdriver    # 导入模块

c = webdriver.Chrome() # 实例 = 类.驱动

c.get('http://cdn1.python3.vip/files/selenium/sample1.html') # 实例.方法

elements = c.find_elements_by_class_name('animal') # 变量 = 实例.方法

for element in elements:
    print(element.text) # text 属性可以获取该元素在网页中的文本内容



# elements和element的区别：
# find_elements:符合条件的 所有 元素，没有符合条件的元素，返回空列表
# find_element:符合条件的 第一个 元素，没有符合条件的元素，抛出-NoSuchElementException异常




