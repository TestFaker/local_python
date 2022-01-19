from api.base_api import BaseApi


class Grouping(BaseApi):

    def add_grouping(self, name):
        """
        添加分组

        :return:
        """
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/create",
            "headers": self.header,
            "json": {"name": name},
        }
        return self.send(data)

    def query_grouping(self):
        """
        查询分组ID

        :return:grouping_id
        """
        data = {
            'method': 'get',
            'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group',
            'headers': self.header,
            'params': {'page': 1,
                       'per_page': 10,
                       'start_time': '2021-12-30',
                       'end_time': '2022-01-13'
                       }
        }
        # return jmespath.search("[?name=='ww'].id", self.send(data).json())
        return self.send(data)

    def add_company(self, **kwargs):
        """
        添加公司

        :return:
        """
        data = {
            'method': 'post',
            'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
            'headers': self.header,
            **kwargs
        }
        return self.send(data)

    def query_company(self, grouping):
        """
        查詢公司ID

        :return:company_id
        """
        data = {
            'method': 'get',
            'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/company-index',
            'headers': self.header,
            'params': {'id': grouping,
                       'keyword': '',
                       'page': '1',
                       'per_page': '10'
                       }
        }
        # return jmespath.search("[?group_id=='19760'].id", self.send(data).json())
        return self.send(data)

    def del_company(self, company_id):
        """
        刪除公司

        :return:
        """
        data = {
            'method': 'get',
            'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/company-delete',
            'headers': self.header,
            'params': {'id': company_id}
        }
        return self.send(data)

    def del_grouping(self, grouping_id):
        """
        刪除分組

        :return:
        """
        data = {
            'method': 'get',
            'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/delete',
            'headers': self.header,
            'params': {'id': grouping_id}
        }
        print(data)
        return self.send(data)
