from selenium import webdriver

biquge = webdriver.Chrome()

biquge.get('https://www.zaobao.com/finance/china/story20200617-1061775')

elements = biquge.find_elements_by_tag_name('p')  # 标签:tag   # 通过tag名来选择元素

for element in elements:
    print(element.text)


