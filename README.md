# laravel-book
laravel 中国网站教程，生成本地文件
## 修改配置文件 App/Config/book.conf
设置生成文件名和爬取教程的路径
## App/Url/Common 设置Cookie
```
def __init__(self):
    config = ConfigTool()
    self.__request_param['headers'] = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'https://laravel-china.org/',
        'Host': 'laravel-china.org',
        'Connection': 'close',
        'Cookie': '',
    }
```