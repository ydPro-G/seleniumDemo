from selenium import webdriver

wb = webdriver.Chrome()

wb.get('https://www.zaobao.com/wencui/politic/story20200716-1069581')



filenam = 'zaobao.txt'

with open(filenam,'w',encoding='utf-8') as f_obj:
    elements = wb.find_elements_by_xpath('//div[@id="FineDining"]/p')
    for element in elements:
        f_obj.write(element.text + '\n')

    

