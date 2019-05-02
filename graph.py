# !bin\env\python 3.6.5
# -*- coding: utf-8 -*-
# author:pzq
import json
from collections import defaultdict
from heapq import *
import queue


def get_node_information():
    """
    顶点信息  相关连的节点信息
    :return: node information
    """
    with open(r"F:\experiment_data\scenery_information.json", 'r', encoding='utf-8') as f:
        content = f.read()
        result = json.loads(content)
        f.close()
        # print("----------------顶点----------------------")
        # num = 1
        # for one in result.items():
        #     # print(f"{one[0]}-{''.join([x for x in one[1].keys()])}")
        #     if str(num) == one[0]:
        #         for x in one[1].items():
        #             print(x[0], x[1])
        return result


def get_edge_information():
    """
    边的信息  路径信息
    :return: path information
    """
    with open(r"F:\experiment_data\scenery_path.json", 'r', encoding='utf-8') as f:
        content = f.read()
        result = json.loads(content)
        f.close()
        # print(result)
        # print("----------------边----------------------")
        # for one in result.items():
        #     for key in one[1].items():
        #         print(f"<v{one[0]},v{key[0]}> {key[1]}")
        return result


def query_dictionary():
    """
    构建出节点和节点的关系
    :return: search dict
    """
    search = {}
    node = get_node_information()
    for one in node.items():
        for x in one[1].keys():
            # dict is a function so only has different key or can has same of value, which is multiple corresponding multiple
            search.update({one[0]: x})
    # print(search)
    return search


def query_scenery_menu():
    """
    通过数字获取对应的景区信息 this is case and translate information in the special domain
    :return:
    """
    search = {}
    num = 2
    edge = get_edge_information()
    node = get_node_information()
    for one in node.items():
        for x in one[1].keys():
            search.update({one[0]: x})
    for one in edge.items():
        if str(num) == one[0]:
            for x in one[1].items():
                for key in search.items():
                    if x[0] == key[0]:
                        print(key[0], key[1], x[1])


def get_array(number):
    """
    将路径信息转化成二维数组
    :number:decide the number is 9999/0 convenience to adjust the param
    :return:
    """
    edge = get_edge_information()
    dimensional = [[number] * len(edge) for _ in range(len(edge))]
    for item in edge.items():
        # print(item)
        for one in item[1].items():
            # print(int(item[0]), int(one[0]), one[1])
            # dimensional.insert([int(item[0]), int(one[0])], one[1])
            dimensional[int(item[0])][int(one[0])] = one[1]
    return dimensional


def dfs(number):
    """
    achieve dfs to search all of the path
    :return:
    """
    length = len(get_array(0))
    array_info = get_array(0)
    print(array_info)
    exit()
    sort_list = [number]
    for j in range(7):
        i = 0
        for i in range(length - 1):
            if array_info[number][i] != 0 and i not in sort_list:
                sort_list.append(i)
            else:
                i += 1
        number = i
        if len(sort_list) == 8:
            break
    print(sort_list)


def dijkstra_raw(edges, from_node, to_node):
    """
    将节点信息和边进行比较获取正确的边集
    :param edges:
    :param from_node:
    :param to_node:
    :return:正无穷大
    """
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    # inf 表示正无穷大
    return float("inf"), []


def dijkstra(edges, from_node, to_node):
    """
    gain the shortest path and this node information
    :param edges: this is a array of path
    :param from_node: start node
    :param to_node: end node
    :return: the shortest path and this node information
    """
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        # 1. Get the length firstly;
        len_shortest_path = length
        # 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        # 2.1 Record the destination node firstly;
        ret_path.append(left)
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            # 2.2 Record other nodes, till the source-node.
            ret_path.append(left)
            right = right[1]
        # 3. Reverse the list finally, to make it be normal sequence.
        ret_path.reverse()
    return len_shortest_path, ret_path


def get_shortest_path(start_node, end_node):
    """
    the shortest_path of matrix
    :param start_node: start_position
    :param end_node: end_position
    :return: the shortest_path
    """
    # endless是不存在边的界限
    endless = 0
    edges_list = []
    m_top = get_array(0)
    for i in range(len(m_top)):
        for j in range(len(m_top[0])):
            if i != j and m_top[i][j] != endless:
                edges_list.append((i, j, m_top[i][j]))  # (i,j) is a link; m_top[i][j] here is 1, the length of link (i,j).
    return dijkstra(edges_list, start_node, end_node)


def kruskal():
    """
    prim 算法
    """
    dimensional = get_array(9999)
    node_num = len(dimensional)
    res = []
    count = 0
    # 获取节点值
    for i in range(node_num):
        for j in range(i):
            if 0 < dimensional[i][j] < 9999:
                count += 1
    # 临界值判断
    if node_num <= 0 or count < node_num - 1:
        return res
    res = []
    selected_node = [0]
    candidate_node = [i for i in range(1, node_num)]
    # 终止条件判断
    while len(candidate_node) > 0:
        begin, end, min_weight = 0, 0, 9999
        for i in selected_node:
            for j in candidate_node:
                if dimensional[i][j] < min_weight:
                    min_weight = dimensional[i][j]
                    begin = i
                    end = j
        res.append([begin, end, min_weight])
        selected_node.append(end)
        candidate_node.remove(end)
    return res


dfs(2)
# prim()
# get_array()
# get_node_information()
# get_edge_information()
# query_scenery_menu()
# query_dictionary()
