# WebDriver对象选择元素的范围是整个Web页面
# WebElement对象 选择元素的范围是 该元素的内部

from selenium import webdriver

we = webdriver.Chrome()

we.get('https://www.zaobao.com/realtime')

element = we.find_element_by_class_name('bananas')
# 限制 选择元素的范围是class为bananas元素的内部
spans = element.find_elements_by_tag_name('span')

for span in spans:
    print(span.text)