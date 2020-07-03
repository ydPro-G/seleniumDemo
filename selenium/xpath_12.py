# Xpath 表达式
print('xpath参考网址：' + 'https://www.w3school.com.cn/xpath/index.asp') # 参考网址

 # Xpath(XML Path Language) 是由国际化标准组织W3C指定的，用来在XML和HTML文档中选择节点的语言

 
 # xpath语法中 ‘/’代表路径；/html/div


 # 绝对路径选择
from selenium import webdriver

wb = webdriver.Chrome()

wb.get('http://cdn1.python3.vip/files/selenium/test1.html')

 # 绝对路径选择
elements = wb.find_elements_by_xpath('/html/body/div')

for element in elements:
    print(element.text) 





# 相对路径选择

 # 在网页中选择某个元素。不管它在什么位置
 # xpath需要在前面加'//'；'//div//p'；从当前节点下寻找所有后代元素，不管它在什么位置


 # 选择所有div元素里面的所有p元素；//div//p
p_all = wb.find_elements_by_xpath('//div//p')
for p_title in p_all:
    print(p_title.text)



 # 选择所有div元素里直接子节点p；'//div/p'
p = wb.find_elements_by_xpath('//div/p')






# 通配符

 # //div/*；选择div元素里所有内容
div_all = wb.find_elements_by_xpath('//div/*')
for divs in div_all:
    print(divs.get_attribute('outerHTML'))







# 根据属性选择
 # 根据属性选择元素格式：[@属性名='属性值']

 # id属性; //*[@id='west']

 # class属性；//*[@class='class_1']
 # class属性；多个属性 //*[@class='class_1 class_2']


 # 根据其他属性；//*[@multiple]









# 按次序选择
 # 选择p类型第2个子元素；//p[2]
 # 选择所有第二个子元素； //div/*[2]

 #某类型倒数子元素
  # 选取p类型倒数第一个子元素； //p[last()]
  # p类型倒数第二个子元素；//p[last()-1]







# 按范围选择[position()<=3]
 # 选额option类型第一个到第二个子元素；//option[position()<=2]  position;位置

 # 选择class属性前三个子元素；//*[@calss='class_1']/*[position()<=3]

 # 选择class属性为multi_choice后三个子元素；//*[class='class_1']/*[position()-2]









# 组选择

 # xpath用 | 隔开多个表达式

  #选择所有option元素和所有h4元素；//option | //h4   =   css   option , h4

  #选择所有class为class_1和class_2的元素；//*[@class='class_1'] | //*[@class='class_2']    =  css   .class_1 , class_2






# 选择父节点
 # 某元素的父节点用；/.. 表示
 #//p[@id='id']/..







# 选择兄弟节点


