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
  # 同时选择多个元素，（.class,div,#id）
ele = wd.find_elements_by_css_selector('div,#BYHY') # 同时选择tag名为div 的元素和id 为BYHY的元素
for e in ele:
    print(e.text)

ts = webdriver.Chrome()
ts.get('http://cdn1.python3.vip/files/selenium/sample1a.html')


acc = ts.find_elements_by_css_selector('#t1 > span , #t1 > p ')# 一个元素里要分开写

for ab in acc:
    print(ab.text)







print("\n")
 # 按次序选择子节点
 # 指定选择的元素是父元素的第几个子节点
 # 直接写:nth-child(2),选择所有为止为2的所有元素，全部类型

 #:nth-child是一個偽類選取器，他看的是順序，縱使你指定了標籤，他依舊會以「順序」作為優先選取的項目，先根据顺序选择指定行，检查它是否是该元素，如果是该元素就做相应的操作

two = ts.find_elements_by_tag_name('#t1 p:nth-child(3)') 

for tw in two:
  print(tw.get_attribute('outerHTML')) 



print("\n")
 # 父元素的倒数第n个子节点
 # nth-last-child
 # p:nth-last-child(1)  选择倒数第一个子元素，并且是p元素

p = ts.find_elements_by_tag_name('p:nth-last-child(2)')
for f in p:
  print(f.get_attribute('outerHTML')) 







 # 父元素的第几个某类型的子节点
 # nth-of-type
 # 选择第一个span类型的子元素
 # span:nth-of-type(1)








 # 父元素的倒数第几个某类型的自己欸按
 # nth-last-of-type





 # 奇数节点和偶数节点
 
 #选择的是父元素的偶数节点 使用 nth-child(even)
 #选择的是父元素的技术节点，使用 nth-child(odd)

#如果要选择的是父元素的 某类型偶数节点，使用 nth-of-type(even)
#如果要选择的是父元素的 某类型奇数节点，使用 nth-of-type(odd)








# 兄弟节点的选择， 元素 + 元素  h3 + span
# 选择元素后面所有的兄弟节点span h3 ~ span

