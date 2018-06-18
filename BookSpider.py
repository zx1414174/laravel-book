from CommonSpider import CommonSpider
from App.Url.Common import Common
import pdfkit
import time
import os
from App.Config.ConfigTool import ConfigTool


class BookSpider(CommonSpider):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    {content}
    </body>
    </html>
    """

    def __init__(self, name, book_url):
        super().__init__()
        self.book_url = book_url
        self.name = name

    def _set_request_tool(self):
        """
        设置请请求基础类
        :return:
        """
        self._request_tool = Common()

    def parse_menu(self, doc):
        section_list = doc('ol.sorted_table > li > ol > li > a')
        menu_list = list()
        for section in section_list.items():
            section_dict = dict()
            section_dict['title'] = section.text()
            section_dict['url'] = section.attr('href')
            menu_list.append(section_dict)
        return menu_list

    def parse_body(self, doc):
        content_doc = doc('div.extra-padding')
        content_doc('p.book-article-meta').remove()
        content_doc('div.pull-right').remove()
        html = self.html_template.format(content=content_doc.html())
        return html.encode('utf-8')

    def run(self):
        doc = self._request_tool.get_pyquery_doc(self.book_url)
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        html_list = []
        book_menu = self.parse_menu(doc)
        for index, menu in enumerate(book_menu):
            file_name = 'book_temp/' + '.'.join([str(index), "html"])
            with open(file_name, 'wb') as f:
                book_doc = self._request_tool.get_pyquery_doc(menu['url'])
                f.write(self.parse_body(book_doc))
            time.sleep(5)
            html_list.append(file_name)
            print(menu)
        pdfkit.from_file(html_list, self.name + ".pdf", options=options)
        for html in html_list:
            os.remove(html)


config = ConfigTool()
book_spider = BookSpider(config.get_config_value('book.basic.name'), config.get_config_value('book.basic.url'))
book_spider.run()

