from selenium import webdriver

wd = webdriver.Chrome()

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')


# css selector  选择语法 可以 联合使用
  # 先指定元素再指定属性值
  # div.footer1 > span.copyright  # 选择一个class属性为copyright的span节点，并且要求是class属性值为fooler1的节点的子节点
  # .footer1 > .copyright 选择 一个class 属性值为copyright 的节点（不限类型）， 并且要求其 必须是 class 属性值为 footer1 的节点的 子节点
  # .footer1 .copyright 子元素同时也是后代元素
elements = wd.find_elements_by_css_selector('div.footer1 > span.copyright')
for a in elements:
    print(a.text) # 




# 组选择
  # ,号
  # 
ele = wd.find_elements_by_css_selector('div,#BYHY') # 同时选择tag名为div 的元素和id 为BYHY的元素
for e in ele:
    print(e.text)

ts = webdriver.Chrome()
ts.get('http://cdn1.python3.vip/files/selenium/sample1a.html')
acc = ts.find_elements_by_css_selector('#t1 > span , #t1 > p ')# 一个元素里要分开写

for ab in acc:
    print(ab.text)