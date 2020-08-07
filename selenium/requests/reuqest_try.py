

# r = requests.get('https://api.github.com/events') # 创建一个名为r的response对象

# # 发送HTTP POST请求

# r = requests.post('http://httpbin.org/post',data={'key':'value'})

# # 发送HTTP PUT请求

# r = requests.put('http://httpbin.org/put',data={'key':'value'})

# # 发送 DELETE 请求

# r = requests.delete('http://httpbin.org/delete')

# # 发送 HEAD 请求

# r = requests.head('http://httpbin.org/get')

# # 发送 OPTIONS请求

# r = requests.options('http://httpbin.org/get')






# 传递Url参数
import requests
payload = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)



# 响应内容
 # 读取服务器响应内容,200
r_text = requests.get('https://api.github.com/events')
print(r_text) # 文本模式：服务器相应内容
print(r_text.content) # 字节模式： 服务器响应内容
print(r.json()) # json模式: 服务器响应内容

print(r_text.encoding) # requests使用的编码
r_text.encoding = 'uft-8'  # 更改requests使用的编码



