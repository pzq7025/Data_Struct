# !bin\env\python 3.6.5
# -*- coding: utf-8 -*-
# author:pzq
from graph import *


# ======================================= 第一部分 ========================================
def create_scenery():
    """
    创建景区景点图
    :return:
    """
    node = get_node_information()
    print(f"顶点数目：{len(node)}")
    print("----------------顶点----------------------")
    for one in node.items():
        print(f"{one[0]}-{''.join([x for x in one[1].keys()])}")

    edge = get_edge_information()
    store_list = []
    print("----------------边----------------------")
    for one in edge.items():
        for key in one[1].items():
            if (key[0], one[0]) not in store_list:
                print(f"<v{one[0]},v{key[0]}> {key[1]}")
                store_list.append((one[0], key[0]))


# ====================================== 第二部分 ==============================================
def query_scenery():
    """
    查询景区 景点信息
    :return:
    """
    print("========  查询景点信息  ========")
    # node is a dict
    node = get_node_information()
    for one in node.items():
        print(f"{one[0]}-{''.join([x for x in one[1].keys()])}")
    while True:
        try:
            num = int(input("请输入想要查找的景点编号(-1退出查询)："))
            if num > 6 or num < -1:
                print("景区不存在！")
            elif num == -1:
                break
            else:
                for one in node.items():
                    if str(num) == one[0]:
                        for x in one[1].items():
                            print(f"{x[0]}\n{x[1]}")
                print('——————————  周边信息  ——————————')
                # edge is a dict and edge information
                edge = get_edge_information()
                # search is a dict and to store information of area and node
                search = query_dictionary()
                # 对对应的节点进行匹配 获取存在的节点
                for one in edge.items():
                    if str(num) == one[0]:
                        for x in one[1].items():
                            # 将数字和景点联系起来
                            for key in search.items():
                                if x[0] == key[0]:
                                    print(f"{search.get(one[0])}——>{key[1]}  {x[1]}")
        except Exception as e:
            _ = e.__cause__
            print("输入错误！请重新尝试！")


# ================================================= 第三部分 =======================================
def scenery_navigation():
    """
    创建景区导航
    :return:
    """
    print("========  旅游景点导航  ========")
    # node is a dict
    node = get_node_information()
    for one in node.items():
        print(f"{one[0]}-{''.join([x for x in one[1].keys()])}")
    while True:
        try:
            num = int(input("请输入当前景点位置(-1退出查询)："))
            if num > 6 or num < -1:
                print("景区不存在！")
            elif num == -1:
                break
            else:
                result = dfs(num)
                search = query_dictionary()
                # print("路线结果：")
                for one in range(len(result)):
                    print(f"第{one + 1}条路径：")
                    for i in result[one]:
                        for key in search.items():
                            # 美化输出
                            if key[0] == str(i) and result[one].index(i) != len(result[one]) - 1:
                                print("{}——>".format(key[1]), end='')
                            if key[0] == str(i) and result[one].index(i) == len(result[one]) - 1:
                                print(key[1])
        except Exception as e:
            _ = e.__cause__
            print("输入错误！请重新尝试！")


# ======================================== 第四部分 ========================================
def search_path():
    """
    搜索最短路径
    :return:
    """
    print("========  搜索最短路径  ========")
    # node is a dict
    node = get_node_information()
    for one in node.items():
        print(f"{one[0]}-{''.join([x for x in one[1].keys()])}")
    while True:
        try:
            start_position = int(input("请输入起始景点的编号(-1退出查询)："))
            if start_position == -1:
                break
            end_position = int(input("请输入结束景点的编号(-1退出查询)："))
            if end_position == -1:
                break
            if start_position > 6 or start_position < -1 or end_position > 6 or start_position < -1:
                print("景区不存在！请重新输入！")
            else:
                print("最短路径为：")
                result = get_shortest_path(start_position, end_position)
                search = query_dictionary()
                for one in result[1]:
                    for key in search.items():
                        # 美化输出
                        if key[0] == str(one) and result[1].index(one) != len(result[1]) - 1:
                            print("{}——>".format(key[1]), end='')
                        if key[0] == str(one) and result[1].index(one) == len(result[1]) - 1:
                            print(key[1])
                print("最短距离为：{}".format(result[0]))
        except Exception as e:
            _ = e.__cause__
            print("输入错误！请重新尝试！")


# ========================================== 第五部分 ======================================
def pave_ruler():
    """
    铺设电路规则
    :return:
    """
    print("========  铺设电路规则  ========")
    result = kruskal()
    search = query_dictionary()
    addition = 0
    for params in result:
        start = ""
        end = ""
        for key in search.items():
            if str(params[0]) == key[0]:
                start = key[1]
        for key1 in search.items():
            if str(params[1]) == key1[0]:
                end = key1[1]
        addition += params[2]
        print("{0} —— {1}  {2}m".format(start, end, params[2]))
    print("铺设电路的总长度为：%sm" % addition)
