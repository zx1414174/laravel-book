from pyquery import PyQuery
import requests
import time


class Common:
    """
    url处理公共类
    """
    # 请求参数
    __request_param = {

    }

    def __init__(self):
        self.__request_param['headers'] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'https://laravel-china.org/',
            'Host': 'laravel-china.org',
            'Cookie': 'remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IkZ6bHdMMGFFWTNvbXAxN1pTb0RuXC9BPT0iLCJ2YWx1ZSI6IkE0R3ROZzNrKzMyazJFNzFYYzhCTFhNdm5ZWVZYbjVYZnBVOTR1WVVEN2ExTWpnQiszY3VTdEFZR2taYnV4RjJncG1DbnBFOWZBODNmcnUwcXhXXC9QMEI0SG4wSWhtRms4XC9uTkZqcUlqaWM9IiwibWFjIjoiYjkxZWU1NTA1YzFlYzk5MmZjNzY3MDIxYmRjZDQ2MTliYTYwMTMxNDJlMDkwNGYzMDM1M2IyZDcwZTA2ZDEyOCJ9; UCToken=731aa15b39d1d3fb1aaeb88a6906aa2eg7CfR3848Nz5RbQl8m9ZGnSpb3H6rORmAShthOY4uG4ojLe4otAyVghjwt2Y; _ga=GA1.2.1026856969.1501318601; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Ikl0VDNud2JPaWtQMFlQQUFXaEVjcUE9PSIsInZhbHVlIjoiSUZSeGJWaVlpWjJMZHFlcGhUdFoyU3ArMjdZZVBUWDA0c3hVc0crUkc3STRMcDE1R1MzQU44Yms2Y0hLNUwwSWZXU0NTTVBURGpaVlA5QnIzcXZyMWlsYlFOXC9hSUVRcjFoR1hRTXArMmtWVjEyU2x6RXQ1ZGVMNWpcL01leWtqSzVnNWMyUmkrNmlBb0xwb0lkNXdqQ29OUnRKTHd5bXViSzFKd1hoUEJsYzlrXC8xSGI0c2poUG9rSUhSTzBhQUJoIiwibWFjIjoiNmU1ZDJlZmIxNGRiYmUxN2Y5MmNiODZmYzA1YmQ1MTZlNjJiNjYwYTI2ZTNmMDUzYzY0NmYzM2VkMmVmNTU1OCJ9; _gat=1; XSRF-TOKEN=eyJpdiI6IlBIMG5PQndRT2F0SFdqbU1SXC9ZZ0lnPT0iLCJ2YWx1ZSI6ImlsOFRBQVVUQ3lwbjkyTmlPXC91eVJvc1daMWRTN2g2OVhGXC9zU29ERXFldkNrOWRadnJOSm0zeDVjQlVNakNjSlwvQTZDRkhcL3B4bzlBUVNZT2tTNWlFZz09IiwibWFjIjoiZjQ3ZWYyM2IyZmFhODNlM2I4ZmI5OGEyZjIyOWFkMjU1ZWEwNjAzMTdiYTNkYmRlNzE0YjFmMDQyZTYxNmNmNSJ9; laravel_session=eyJpdiI6InF4cm5Fd0tlK05JTHg2T2t1d3ZkaHc9PSIsInZhbHVlIjoib1QzS0VsZUVFdlwveVBTTm1hV29cL1wvV2NRVVVHMlZNZWw5Q2Vjclp2YmVKZUZjUzdudmt6TlNKa0dvSE9VNFpqcnNUODkzM3pmMUUzanYrVGhZbktJbEE9PSIsIm1hYyI6IjhlMzNkYTVlMjk5NDZiNjFlZjYwMTU0ODJjNGM5YTA4M2FhN2E2YzdmNzVkNmY1NzZjMWY2Mjk1N2NhMjFhZjEifQ%3D%3D'
        }

    def get_pyquery_doc(self, url, headers=''):
        """
        获取pyquery处理doc
        :param str url:
        :param dict headers:
        :return:
        """
        doc = False
        url_response = self.get_url_response(url, headers)
        if url_response:
            doc = PyQuery(url_response.text)
        return doc

    def get_url_response(self, url, headers=''):
        """
        获取链接请求文本
        :param str url:
        :param dict headers:
        :return:
        """
        request_param = self.__request_param
        request_param['timeout'] = 3
        request_param['url'] = url
        try:
            if headers != '':
                request_param['headers'] = headers
            url_response = requests.get(**request_param)
            if url_response.status_code != 200:
                return False
        except:
            url_response = False
        return url_response

    def get_repeat_url_response(self, url, repeat_num=3):
        """
        重复请求
        :param str url:
        :param int repeat_num:
        :param dist headers:
        :return:
        """
        url_response = False
        for i in range(repeat_num):
            url_response = self.get_url_response(url)
            if url_response:
                break
        return url_response

    def get_headers(self):
        """
        获取请求头配置
        :return Dict:
        """
        return self.__request_param['headers']

    def set_header(self, headers):
        """
        设置请求头
        :param headers:
        :return:
        """
        self.__request_param['headers'] = headers
        return self

    def set_proxies(self, proxies):
        """
        设置proxies type
        :param dict proxies:
        :return:
        """
        self.__request_param['proxies'] = proxies
        return self

    def del_proxies(self):
        self.__request_param.pop('proxies')
        return self

    def set_request_param(self, request_param):
        """
        设置
        :param request_param:
        :return:
        """
        self.__request_param.update(request_param)
        return self



