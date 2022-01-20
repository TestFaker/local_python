import json

import jmespath
import pytest

from api.ai_list import AiList
from api.grouping import Grouping


class TestGrouping:
    def setup_class(self):
        self.group = Grouping()
        self.list = AiList()

    # def test_query_grouping(self):
    #     """
    #     查詢分組id
    #     :return:
    #     """
    #     query_response = self.group.query_grouping()
    # @pytest.mark.smoke
    @pytest.mark.parametrize("name", ['ww'], ids=["ONE"])
    def test_1_grouping(self, name):
        """
        添'刪'分組
        :return:
        """
        add_response = self.group.add_grouping(name)
        # print(json.dumps(add_response.json(), indent=1, ensure_ascii=False))
        grouping_id = jmespath.search("id", add_response.json())
        # print(grouping_id)
        del_response = self.group.del_grouping(grouping_id)
        # print(del_response.json())
        assert jmespath.search('ok', add_response.json()) is False

    @pytest.mark.parametrize("name", ['ww'], ids=["ONE"])
    def test_2_grouping(self, name):
        """
        添加分組，添加公司，刪除公司，刪除分組
        :return:
        """
        add_grouping_response = self.group.add_grouping(name)
        grouping_id = jmespath.search("id", add_grouping_response.json())
        add_company_response = self.group.add_company(grouping_id)
        company_id = jmespath.search("id", add_company_response.json())
        delete_company_response = self.group.del_company(company_id)
        delete_grouping_response = self.group.del_grouping(grouping_id)

    def test_ai_list(self):
        ai_list_response = self.list.ai_list()
        # print(json.dumps(ai_list_response.json(), indent=4, ensure_ascii=False))
        assert jmespath.search('ok', ai_list_response.json()) is False
        more_response = self.list.more()
        # print(json.dumps(more_response.json(), indent=4, ensure_ascii=False))

        # print(json.dumps(add_response.json(), indent=1, ensure_ascii=False))

    # @pytest.mark.parametrize("name", ['ww'], ids=["ONE"])
    # def test_add_grouping(self, name):
    #     """
    #     添加分組，查詢分組
    #     :return:
    #     """
    #     add_response = self.group.add_grouping(name)
    #     # print(json.dumps(add_response.json(), indent=1, ensure_ascii=False))
    #     assert jmespath.search('name', add_response.json()) == 'ww'
    #     assert jmespath.search('created_by', add_response.json()) == 181
    # @pytest.mark.smoke
    # def test_all_group(self):
    #     self.group.add_grouping("小王")
    #     r = self.group.get_list(1)
    #     id = self.group.jsonpath("[?name=='小王'].id", r.json())
    #     logger.info(id)
    #     self.group.company_create(id)
    #     r = self.group.delete_group(id)
    #     assert r.json() == True
