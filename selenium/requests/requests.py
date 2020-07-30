import requests

r = requests.get('https://api.github.com/events') # 创建一个名为r的response对象

# 发送HTTP POST请求

r = requests.post('http://httpbin.org/post',data={'key':'value'})

# 发送HTTP PUT请求

r = requests.put('http://httpbin.org/put',data={'key':'value'})

# 发送 DELETE 请求

r = requests.delete('http://httpbin.org/delete')

# 发送 HEAD 请求

r = requests.head('http://httpbin.org/get')

# 发送 OPTIONS请求

r = requests.options('http://httpbin.org/get')