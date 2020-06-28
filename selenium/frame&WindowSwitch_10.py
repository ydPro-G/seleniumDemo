# frame切换/窗口切换
from selenium import webdriver

wd = webdriver.Chrome()

wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')






# iframe元素非常特殊，frame或iframe元素内部会包含一个被嵌入的另一份html文档

# 如果要操作 被嵌入的html文档中的元素，就必须 切换操作方位 到 被嵌入的文档中

# 使用WebDriver对象的switch_to属性 switch.to.frame(id,name)

wd.switch_to.frame('innerFrame')

elements = wd.find_element_by_class_name('plant')
print(elements.text)



# 如果已切换到某个iframe操作，那么后续的选择和操作界面元素就都在这个frame进行

# 切换到主HTML，实例.switch_to.default_contet()
wd.switch_to.default_content()
wd.find_element_by_id('outerbutton').click()
wd.quit()











 # 切换到新的窗口

 # 会遇到，点击一个 链接 或 按钮，会打开一个新窗口
 # 这时候会遇到问题，新窗口打开了但是WebDriver对象对应的还是老窗口，自动化操作也是在老窗口进行
from selenium import webdriver
wb = webdriver.Chrome()



wb.get('http://cdn1.python3.vip/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wb.find_element_by_tag_name("a").click()

print(wb.title) # 返回的是原窗口的字段




# 如何切换到新窗口？
# 可以使用WebDriver对象的 switch_to 属性的 window 方法
# wb.wsitch_to.windows(handle)
# handle 要传什么？传当前浏览器里所有的窗口句柄（窗口id）

hand = webdriver.Chrome()
hand.implicitly_wait(5)
hand.get('http://cdn1.python3.vip/files/selenium/sample3.html')

mainWindow = hand.current_window_handle # 用一个变量保存当前窗口的句柄

lina = hand.find_element_by_tag_name("a").click()
for handle in hand.window_handles: # window_handles属性获取当前所有网页窗口句柄，然后以列表的形式存储
    hand.switch_to.window(handle)
    if '必应' in hand.title: # 根据标题栏或地址栏
        break # 跳出循环，然后在新窗口操作
hand.find_element_by_id('sb_form_q').send_keys('bing')


# 新窗口操作完后使用mainWindow变量返回到原窗口
hand.switch_to.window(mainWindow) # 原窗口句柄
print(hand.title)
