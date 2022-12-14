# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/11 20:46'

class Tree(object):
    def __init__(self, data,parentautoid=0):
        self.parentautoid = parentautoid
        self.data = data
        self.root_node = list()
        self.common_node = dict()
        self.tree = list()

    def find_root_node(self, ) -> list:
        """
        查找根节点
        :return:根节点列表
        """
        # self.root_node = list(filter(lambda x: x["father_id"] is None, data))
        for node in self.data:
            # 假定father_id是None就是根节点，例如有些数据库设计会直接把根节点标识出来。
            if node["parent"] == self.parentautoid:
                self.root_node.append(node)
        return self.root_node

    def find_common_node(self) -> dict:
        """
        寻找共同的父节点
        :return: 共同的父节点字典
        """

        for node in self.data:
            father_id = node.get("parent")
            # 排除根节点情况
            if father_id is not None:
                # 如果父节点ID不在字典中则添加到字典中
                if father_id not in self.common_node:
                    self.common_node[father_id] = list()
                self.common_node[father_id].append(node)
        return self.common_node

    def build_tree(self, ) -> list:
        """
        生成目录树
        :return:
        """
        self.find_root_node()
        self.find_common_node()
        for root in self.root_node:
            # 生成字典
            base = dict(name=root["name"], id=root["id"], child=list())
            # 遍历查询子节点
            self.find_child(base["id"], base["child"])
            # 添加到列表
            self.tree.append(base)
        return self.tree

    def find_child(self, father_id: int, child_node: list):
        """
        查找子节点
        :param father_id:父级ID
        :param child_node: 父级孩子节点
        :return:
        """
        # 获取共同父节点字典的子节点数据
        child_list = self.common_node.get(father_id, [])
        for item in child_list:
            # 生成字典
            base = dict(name=item["name"], id=item["id"], child=list())
            # 遍历查询子节点
            self.find_child(item["id"], base["child"])
            # 添加到列表
            child_node.append(base)


data = [{'id':1,'parent':0,'name':'目录1'},
        {'id':2,'parent':0,'name':'目录2'},
        {'id':3,'parent':0,'name':'目录3'},
        {'id':4,'parent':0,'name':'目录4'},
        {'id':5,'parent':1,'name':'目录1.1'},
        {'id':6,'parent':1,'name':'目录1.2'},
        {'id':7,'parent':1,'name':'目录1.3'},
        {'id': 8, 'parent': 2, 'name': '目录2.1'},
        {'id':9,'parent':2,'name':'目录2.2'},
        {'id':10,'parent':3,'name':'目录3.1'},
        {'id':11,'parent':3,'name':'目录3.2'},
        {'id':13,'parent':5,'name':'目录1.1.1'},
        {'id': 14, 'parent': 9, 'name': '目录2.2.1'},
        {'id': 15, 'parent': 8, 'name': '目录2.2.2'},
        ]


tree = Tree(data=data, parentautoid=2)
rest = tree.build_tree()
print(rest)