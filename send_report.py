import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://admin:Aa123456!@59.110.165.85:9000/job/Ai_API/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=0bb61434d5d1caadbd63d10ba8108bc32227bab03b6e0df7f1e3ab329649248b'

        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号admin,密码Aa123456!",
                    "title": ",0" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://admin:Aa123456!@59.110.165.85:9000/job/Ai_API/allure/"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
