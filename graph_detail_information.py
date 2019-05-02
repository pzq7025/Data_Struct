# !bin\env\python 3.6.5
# -*- coding: utf-8 -*-
# author:pzq
import json

path = {
    0: {2: 700, 4: 1000, 5: 600},
    1: {2: 1000, 6: 1000},
    2: {3: 400, 0: 700, 1: 1000},
    3: {4: 300, 6: 400, 2: 400},
    4: {5: 600, 0: 1000, 3: 300},
    5: {6: 500, 0: 600, 4: 600},
    6: {5: 500, 1: 1000, 3: 400},
}
information = {
    0: {'A区': '北国风光，千里冰封，万里雪飘'},
    1: {'B区': '大漠孤烟直，长河落日圆'},
    2: {'C区': '塞上秋来风记忆，衡阳雁去无留意'},
    3: {'D区': '阡陌交通，其中往来种做，男女衣着，悉如外人'},
    4: {'E区': '世界本没有路，走的人多了，也就成了路'},
    5: {'F区': '我如黎明中的光芒，在此绽放'},
    6: {'G区': '星分翼轸，地接衡庐'},
}
with open(r"F:\experiment_data\scenery_path.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(path))
    f.close()
# with open(r"F:\experiment_data\scenery_information.json", 'w', encoding='utf-8') as f:
#     f.write(json.dumps(information))
#     f.close()
