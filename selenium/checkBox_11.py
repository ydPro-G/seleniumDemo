# 常见的选择框包括：radio,checkbox，select




print("\nradio")
# radio框
 # 直接模拟用户点击就可以
from selenium import webdriver
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome()


wd.get('http://cdn1.python3.vip/files/selenium/test2.html')


# 获取当前选中的元素
elements = wd.find_element_by_css_selector(
    '#s_radio > input[value=小雷老师]'
)

print("当前选中的是" + elements.get_attribute('value')) # .get_attribute获取元素标签的内容；获取元素内全部HTML('innerHTML'；获取包含选中元素的HTML('outerHTML')


# 点击选中的radio框
wd.find_element_by_css_selector(
    '#s_radio > input[value="小雷老师"]'
).click()







print("\ncheckbox")
# checkbox框
 # 直接模拟用户点击
 # 要选中checkbox的一个选项，先获取当前复选框的状态
 # 可以将 已选中的选项 全部点击一下，确保都是 未选状态


# 将已选中的选项点击，恢复未选中状态
check_elements = wd.find_element_by_css_selector(
    '#s_checkbox > input[checked=checked]'
).click()


# 点击选中的checkbox框
wd.find_element_by_css_selector(
    '#s_checkbox > input[value=小雷老师]'
).click()







print("\nselect")
# select框是一个新的select标签
 # select可以使用select_by_value,根据选项的value属性值，选择元素

 # select_by_index，根据选项次序(0),选择元素
 #select_by_visible_text，根据选项的可见文本，选择元素
from time import sleep
sleep(3)

# select单选框

#from selenium.webdriver.support.ui import Select 导入select类
selects = Select(wd.find_element_by_id('ss_single'))

selects.select_by_visible_text('小雷老师')




# select多选框

# deselect_by_value # 根据value属性值，取消选定的元素

# deselect_by_index # 取消选定的元素，按照选项的次序

# deselect_by_visible_text # 根据选项的可见文本，取消选定的元素

# deselect_all 去除选中所有元素

# 创建select类
se = Select(wd.find_element_by_id('ss_multi'))

# 清除所有选中的选项
se.deselect_all()

# 选择小雷老师和小凯老师
se.select_by_visible_text('小雷老师')
se.select_by_visible_text('小凯老师')