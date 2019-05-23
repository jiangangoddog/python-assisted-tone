# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:25:38 2019

@author: 32027
"""

import pandas as pd
import numpy as np
import re
from prettytable import PrettyTable

def find_pitch(tune, target_tune):#核心函数，功能有：1、将原曲每个音符变调，输出新调式；2、计算各调式半音数量；3、计算各调式最高音和最低音
    Index = tune[target_tune].reset_index(drop=True)#目标调式目录，由低到高，用于比较音高
    Min = len(Index)#初始化最低音高索引
    Max = 0#初始化最高音高索引
    Tune = []#初始化新目标调式曲谱
    count = 0#初始化半音计数器
    for note in music:#每个音符依次变调
        if any(index in note for index in tune.index):#判断是否是音符字符串
            MAX = 0#初始化匹配选择器
            for index in tune.index:#沿原调式依次搜索
                if index in note:#筛选出原调式所有匹配音调
                    length = len(index)#输出匹配音调长度
                    if length >= MAX:#选择最长的匹配音调为正确匹配音调
                        MAX = length
                        Note = tune.loc[index,target_tune]#匹配目标音调
                        NOTE = note.replace(index,Note)#为目标音调添加回原音调字符串其他内容
                    else:
                        continue
                else:
                    continue
            ind = Index[Index.values == Note].index.values[0]#返回目标音调目录索引
            if Min>=ind:
                Min = ind#计算最低音调索引
            if Max<=ind:
                Max = ind#计算最高音调索引
            if '#' in Note:
                count+=1#计算半音数
        else:
            NOTE = note#非音符字符串，直接复制
        Tune.extend([NOTE])#拼接生成目标调式曲子

    highest = Index[Max]#得出最高音调
    lowest = Index[Min]#得出最低音调
    return Tune, highest, lowest, count#返回新调式曲子、最高、最低音调、半音数


def output(final_tune='C'):#输出目标调式曲子
    if final_tune == initial_tune:
        raise NameError('新调式不能与原调式相同')
    for i in range(len(globals()[final_tune])):#增加换行符
        if re.match('\w:',globals()[final_tune][i]) != None:
            globals()[final_tune][i] = '\n'+globals()[final_tune][i]
    with open('result.txt','w',newline='',encoding="utf-8") as file:
        globals()[final_tune] = ' '.join(globals()[final_tune])#将list拼接成空格分割的string
        globals()[final_tune] = globals()[final_tune].replace(initial_tune, final_tune).replace('升','#')#更改新调式符号
        file.write(globals()[final_tune][1:])#输出新调式曲子，删除第一行空行
        file.close()#关闭文件

tune = pd.read_excel('tone.xlsx').astype(str)#读取调式对照表
music = open('music.txt',encoding='utf-8').read()#读取标准化格式曲谱脚本
initial_tune = re.search('D: (.*)\n',music).group(1)#读取原曲调式
music = music.replace('\n',' ').split(' ')#将string变为list，方便后续操作

tune = tune.set_index(initial_tune)#将原调式设为索引
result = PrettyTable()#初始化图表
result.field_names = (['调式','最高音','最低音','半音数'])#绘制表头
for target_tune in np.array(tune.columns).tolist():
    globals()[target_tune], highest, lowest, count = find_pitch(tune, target_tune)#计算各调式相关
    result.add_row([target_tune, highest, lowest, count])#绘制各目标调式比较表
result.align = "l"#表格左对齐
result.padding_width = 1#表格内部间距
print(result)#输出表格

#output()#生成所需调式曲谱脚本，默认为C调,可选'C', '升C', 'D', '升D', 'E','F','升F', 'G', '升G', 'A', '升A', 'B'中除原调外的曲调。
