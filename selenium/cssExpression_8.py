# css 选择器
from selenium import webdriver

css = webdriver.Chrome()

css.get('http://cdn1.python3.vip/files/selenium/sample1.html')


# 通过css selector选择单个元素：find_element_by_css_selector(css selector参数)

# 通过css selector选择多个元素：find_elements_by_css_selector(css selector参数)



# Css Selector 同样可以根据tag名，id属性和class属性来选择元素

element = css.find_elements_by_css_selector('div') # 选择所有tag名为div的元素
for e in element:
    print(e.text)  





# css  id属性选择
# 加#
# find_element_by-css_selector('#id_name')

id_a = css.find_element_by_css_selector('#searchtext').send_keys('你好')






# css class属性选择
# 加.
# find_elements_by_css_selector('.class_name')
class_a = css.find_elements_by_css_selector('.animal') # 选择所有class属性为animal的元素，输出
for cl in class_a:
    print(cl.text)







# 选择子元素和后代元素
# 子元素：元素1 > 元素2 > 元素3 > 元素4
# 后代元素：元素1   元素2   元素3  元素4





print("\ncss通过属性来选择元素")
# css  通过属性来选择元素
# 加[]
# find_element_by_css_selector('["attribute"]')
attribute = css.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

print(attribute.get_attribute('outerHTML'))  # 打印出元素对应的html


  # 加上标签名      限制
  # div[class='SKnet']
  # 选择所有标签名为div，且calss属性值为SKnet的元素



  # 只选择属性值
  # [href]，选择   所有    具有属性名为href的元素


  # 选择属性值    包含    某个字符串的元素
  #a[href*=miitbenian]，选择a节点里面href属性包含miitbeian字符串

 
  # 选择属性值 以某个字符串     开头    的元素
  # a[href^="http"]，选择a节点里面href属性以http开头
ht = css.find_element_by_css_selector('a[href^="http"]')
print(ht.get_attribute('outerHTML'))


  # 选择属性值 以某个字符串    结尾    的元素
  # a[href$="gov.cn"]，选择a节点里面href属性以gov.cn结尾


  # 如果一个元素具有       多个属性
  # 需要具有多个属性限制div[class=misc][type=gun]






# 验证
# F12,CTRL+F,输入
# #bottom > .footer2 a
# id(父元素) > class(子元素) a(后代元素)