from CommonSpider import CommonSpider
from App.Url.Proxy import Proxy


class BookSpider(CommonSpider):
    def _set_request_tool(self):
        """
        设置请请求基础类
        :return:
        """
    self._request_tool = Proxy()
