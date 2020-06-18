from selenium import webdriver

bqg = webdriver.Chrome()

bqg.get('http://www.ibqg5200.com/paihang.html')


elements = bqg.find_element_by_class_name('index_toplist')
spans = elements.find_element_by_tag_name('a') # find_element获取的是第一个元素，所以用for循环报错，因为只有一个元素

print(spans.text) # 直接输出，注意加.text以文本模式输出


spans_a = elements.find_elements_by_tag_name('a') # find_selements获取的是一个列表，所以要使用for循环来输出列表元素

for span in spans_a:
    print(span.text) # 使用for循环，让Python将列表中的元素，存储到变量中，接下来循环这个操作，直到列表没有元素为止

    