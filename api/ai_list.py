from api.base_api import BaseApi


class AiList(BaseApi):
    def ai_list(self):
        """
        舆情列表

        :return:
        """
        data = {
            "method": "post",
            "url": 'http://123.56.138.96:3012/api/ainews-espy/api/opinion/v2/article-list',
            "headers": self.header,
            "json": {
                "sort_by": "pub_time",
                "sort_order": "desc",
                "page": 1,
                "board": "main",
                "classification": "",
                "category_key": "",
                "cp_type": "1",
                "article_type": "all",
                "risk_level": [0, 1, 2],
                "start_time": "2022-01-04T00:00:00",
                "end_time": "2022-01-10T22:31:24"
            },
        }
        return self.send(data)

    def more(self):
        """
        more更多按钮

        :return:grouping_id
        """
        data = {
            'method': 'post',
            'url': 'http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news',
            'headers': self.header,
            'params': {"start_time": "2022-01-04T08:57:49",
                       "end_time": "2022-01-11T08:57:49",
                       "page": 1,
                       "pagesize": 20}
        }
        return self.send(data)