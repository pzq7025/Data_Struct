# !bin\env\python 3.6.5
# -*- coding: utf-8 -*-
# author:pzq
from part_function import *


def menu():
    while True:
        content = "1.创建景区景点图\n2.查询景点信息\n3.旅游景点导航\n4.搜索最短路径\n5.铺设电路规则\n0.退出"
        print("=========  景区管理系统  =========")
        print(content)
        try:
            num = int(input("请输入操作编号（0~5）:"))
            if num == 1:
                # print("顶点数目：")
                create_scenery()
            elif num == 2:
                # print("查询景点信息")
                query_scenery()
            elif num == 3:
                # print("旅游景点导航")
                scenery_navigation()
            elif num == 4:
                # print("搜索最短路径")
                search_path()
            elif num == 5:
                # print("铺设电路规则")
                pave_ruler()
            elif num == 0:
                exit()
            else:
                print("输入指令不在操作范围内!")
        except Exception as e:
            # print(e)
            _ = e.__cause__
            print("非法输入！")


if __name__ == '__main__':
    menu()
