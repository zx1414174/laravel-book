from CommonSpider import CommonSpider
from App.Url.Proxy import Proxy


class BookSpider(CommonSpider):
    def __init__(self, book_url):
        super().__init__()
        self.book_url = book_url

    def _set_request_tool(self):
        """
        设置请请求基础类
        :return:
        """
        self._request_tool = Proxy()

    def parse_menu(self, doc):
        doc = self._request_tool.get_url_response(self.book_url)
        with open('test.html', 'wb') as f:
            f.write(doc.text.encode('utf-8'))
        # tr_doc_list = doc('#ip_list > tr')

    def run(self):
        doc = self._request_tool.get_pyquery_doc(self.book_url)
        book_menu = self.parse_menu(doc)
        # with open('test.html', 'wb') as f:
        #     f.write(doc.text.encode('utf-8'))


book_spider = BookSpider('https://laravel-china.org/courses/laravel-advance-training-5.5/806/introduction-of-api-automation-test')
book_spider.parse_menu()

