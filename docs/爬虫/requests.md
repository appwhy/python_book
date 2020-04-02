# requests 模块

[TOC]

---

requests主要有6个方法：**get**，head，put（覆盖），**post（追加）**，patch（局部修改），delete。

## Request

requests.get(url, params=None, **kwargs) 

**kwargs参数：**

1. params : 字典或字节序列，作为参数增加到url中
2. data : 字典、字节序列或文件对象，作为Request的内容
3. json : JSON格式的数据，作为Request的内容
4. headers : 字典，HTTP定制头
5. cookies : 字典或CookieJar，Request中的cookie
6. auth : 元组，支持HTTP认证功能
7. files : 字典类型，传输文件
8. timeout : 设定超时时间，秒为单位
9. proxies : 字典类型，设定访问代理服务器，可以增加登录认证
10. allow_redirects : True/False，默认为True，重定向开关
11. stream : True/False，默认为True，获取内容立即下载开关
12. verify : True/False，默认为True，认证SSL证书开关
13. cert : 本地SSL证书路径

### requests设置代理

```python
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
requests.get("https://www.baidu.com/", proxies=proxies)
```

### https 证书验证

```python
url = 'https://kyfw.12306.cn/otn/leftTicket/init'

# 关闭证书验证
r = requests.get(url, verify=False)

# 开启证书验证
r = requests.get(url, verify=True)
r = requests.get(url, verify= '/path/to/certfile')  # ?设置证书所在路径
```



## Response（requests.models.Response）

常用属性：

* status_code：状态码
*  headers：一个字典
*  encoding：从http header中获取，可能不准。
* apparent_encoding：从内容中获取编码格式，比较耗时。
* content：http响应内容的二进制格式。
*  text：响应内容的字符串格式。

常用方法：

* res.raise_for_status：如果状态码不是200，就产生异常requests.HTTPError。
* json：返回json响应内容。





## requests爬取网页的一般框架

### 爬取网页

```python
import requests

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'
```



### 爬取图片

```python
def get_image(url, image_path):
    r = reqquests.get(url)
    with open(image_path, 'wb') as f:
        f.write(r.content)
```

加载图片：

```python
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))
```



## Session

Session对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie。

注：如果把cookies或headers放进请求参数中，在session进行第一次请求后，这些参数不会自动添加到后续的请求中。因此，为了是参数在session中共用，应该将其添加到session上。

```python
session = requests.session()
session.cookies = get_cookiejar()
session.headers = {}
session.get('https://www.baidu.com')
```





## Cookie

cookies需要是 requests.cookies.RequestsCookieJar，是 http.cookiejar.CookieJar 的子类。二者的Cookie都是http.cookiejar.Cookie。

使用cookie：

```python
import requests

url = 'https://movie.douban.com/'
r = requests.get(url)
mycookies = r.cookies   # RequestsCookieJar对象
print(mycookies)

# RequestsCookieJar转换字典
cookies_dict = requests.utils.dict_from_cookiejar(mycookies)
print(cookies_dict)

# 字典转换RequestsCookieJar
cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict, cookiejar=None, overwrite=True)
print(cookies_jar)

# 在RequestsCookieJar对象中添加Cookies字典
requests.utils.add_dict_to_cookiejar(mycookies, cookies_dict)
```

