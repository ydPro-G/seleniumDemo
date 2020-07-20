# import requests

# response = requests.get('http://mirrors.sohu.com/')
# print(response.text) # http响应消息体中的文本内容


# 构建请求url参数

# import requests

# urlpara = {
#     'wd':'iphone&ipad',
#     'rsv_spt':'1'
# }
# response = requests.get('https://www.baidu.com',params=urlpara)

# print(response.text)











# # 构建请求消息头

# import requests
# headers = {
#     'user-agent': 'my-app/0.0.1',
#     'auth-type': 'jwt-token'
# }

# r = requests.post("http://httpbin.org/post",headers=headers)
# print(r.text)










# 构建请求消息体
#  json格式消息体

# import requests,json

# payload = {
#     "Overall":"良好",
#     "Progress":"30",
#     "Problems":[
#         {
#             "No":1,
#             "desc":"问题1...."
#         },
#         {
#             "No":2,
#             "desc":"问题2...."
#         },
#     ]
# }

# r = requests.post("http://httpbin.org/post",data=json.dumps(payload)) # 使用json库的dumps方法
# r = requests.post("http://httpbin.org/post",json=payload) # 也可以将数据对象直接传递给post方法的json参数











# 检查HTTP响应

#  # 检查HTTP响应状态码，通过reponse对象status_code属性获得
# import requests

# response =requests.get("http://mirrors.sohu.com/aaaa")
# print(response.status_code) # .status_code获得HTTP响应的状态







# 检查响应消息头
# 通过headers属性获取

# import requests

# response = requests.get('http://mirrors.sohu.com/')
# print(type(response.headers))  # 获取响应消息头类型
# print(dict(response.headers))  # 获取相应消息头字典内容

# print(response.headers['Content-Type']) # response.headers对象的类型是 继承自Dict字典类型的一个类，我们可以像操作字典一样操作它








# 检查响应消息体
 # 通过text属性获得

import requests

response = requests.get('http://mirrors.sohu.com/')
response.encoding='utf-8' # 指定编码格式
print(response.text) # text 获取响应消息体
print(response.content.decode('utf-8')) # 内容解码

# json
responses = requests.post("http://httpbin.org/post",data={1:1,2:2})
obj = responses.json() # 处理响应消息中json格式的数据，将json格式的数据字符串转化为数据对象
print(obj)

