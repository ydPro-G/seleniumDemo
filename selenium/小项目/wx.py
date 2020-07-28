from selenium import webdriver

wb = webdriver.Chrome()

wb.get('https://www.zaobao.com/realtime/china/story20200728-1072639')

message = wb.find_elements_by_xpath('//p')
for messag in message:
    print(messag.text)