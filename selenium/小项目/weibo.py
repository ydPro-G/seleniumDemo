from selenium import webdriver

wb = webdriver.Chrome()

wb.get('https://s.weibo.com/top/summary?cate=realtimehot')


filename = 'weibo.txt'

with open(filename,'w') as f_obj:
    elements = wb.find_elements_by_xpath('//tbody/tr/td/a')
    for element in elements:
        f_obj.write(element.text + '\n')
    
    links = wb.find_elements_by_xpath('//tbody/tr/td/*[@href]')
    for link in links:
        f_obj.writelines('link: ' + link.get_attribute('href') + '\n')
    

     


    
    
        
    










