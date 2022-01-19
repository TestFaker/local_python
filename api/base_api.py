import os

import requests
import yaml
from loguru import logger


class BaseApi:
    def __init__(self):
        self.header = {"Content-Type": "application/json;charset=UTF-8",
                       "Authorization": self.get_token()}

    def send(self, data):
        response = requests.request(**data)
        # print(json.dumps(response.json(), indent=1, ensure_ascii=False))
        return response

    # def logger(self):
    #     print(__file__)
    #     print(os.path.abspath(__file__))
    #     path = os.path.dirname(os.path.abspath(__file__))
    #     logger.add(os.path.expanduser(path + r"/test_logs.log"))

    def get_token(self):
        """
       提取token

       :return:
       """
        data = {
            'method': 'post',
            'url': 'http://123.56.138.96:3012/api/ainews-user/user/login',
            'headers': {"Content-Type": "application/json;charset=UTF-8"},
            'json': {"name": "lsj1", "password": "123123"},
        }
        return self.send(data).json().get("access_token")

    # @staticmethod
    # def yaml_parser(path):
    #     with open(path, "r", encoding="utf-8") as f:
    #         return yaml.safe_load(f)

    # if __name__ == '__main__':
    #     print(BaseApi().yaml_parser("/Applications/code/AutoAi/case/test_grouping.yaml").get("test_delete_group"))
