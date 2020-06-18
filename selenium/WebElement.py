# WebDriver对象选择元素的范围是整个Web页面
# WebElement对象 选择元素的范围是 该元素的内部

from selenium import webdriver

we = webdriver.Chrome()
we.get('http://cdn1.python3.vip/files/selenium/sample1.html')

element = we.find_element_by_id('container')

spans = element.find_elements_by_tag_name('span')  # span：范围

for span in spans:
    print(span.text)