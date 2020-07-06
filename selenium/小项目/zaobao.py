from selenium import webdriver

wb = webdriver.Chrome()

wb.get('https://www.zaobao.com')

filename = 'zaobao.txt'

with open(filename,'w',encoding='utf-8') as file_object:

    elements = wb.find_elements_by_xpath('//ul[@class="bananas"]/li/div/a/span')

    for element in elements:
        nolist = element.get_attribute('innerText')  # innerHTML会返回元素内部的HTML，包含所有的HTML标签。
                                                     #textContent和innerText置灰得到文本内容，而不会包含HTML标签。textContent是W3C兼容的文字内容属性，但是IE不支持；innerText不是W3C DOM的指定内容，但是FireFox不支持。

        file_object.write(nolist + '\n')   # 在循环里才能把所有的信息循环出来







# //ul[@class="bananas"]/li/div/a/span


# .bananas > li >div > a > span