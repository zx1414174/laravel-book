from pyquery import PyQuery
import requests
from App.Config.ConfigTool import ConfigTool


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
            'Connection': 'close',
            'Cookie': '',
        }

    def get_pyquery_doc(self, url, headers=''):
        """
        获取pyquery处理doc
        :param str url:
        :param dict headers:
        :return:
        """
        doc = ''
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
        request_param['timeout'] = 20
        request_param['url'] = url
        # try:
        if headers != '':
            request_param['headers'] = headers
        url_response = requests.get(**request_param)
        if url_response.status_code != 200:
            return False
        # except:
        #     url_response = False
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



