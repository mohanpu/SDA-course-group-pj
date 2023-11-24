#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 01:01:54 2023

@author: black
"""

import pandas as pd #用于数据处理和读取 Excel 文件。
from wordcloud import WordCloud #用于生成词云图。
import numpy as np #用于处理数组数据。
from PIL import Image #用于处理图像数据。
import jieba
import jieba.analyse
import jieba.posseg


from collections import Counter
import re
#添加inchinese辅助函数，排除其他字符、数字干扰

def is_chinese(word):
    # 判断是否为中文字符
    return bool(re.search('[\u4e00-\u9fa5]', word))


def count_word_frequency(txt_path):
    # 打开TXT文件，读取文本内容
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 使用jieba分词
    words = jieba.cut(text)

    # 滤掉长度过小的连接词
    words = [word for word in words if len(word) > 1]

    # 使用Counter统计词频
    word_counter = Counter(words)

    return word_counter

def main():
    # 指定TXT文件的路径
    txt_path = '/Users/black/Desktop/大二上/SDA/SDAmer/23mergedbyyr.txt'

    # 获取词频统计结果
    word_frequency = count_word_frequency(txt_path)
    word_list = []  # 创建空的词语列表
    frequency_list = []  # 创建空的频率列表
    # 打印词频统计结果
    for word, frequency in word_frequency.items():
        if frequency > 1:
           # 创建一个 DataFrame
           word_list.append(word)
           frequency_list.append(frequency)
           data = {'词语': word_list, '次数': frequency_list}
           df = pd.DataFrame(data)
           save_path = '/Users/black/Desktop/大二上/SDA/23高频词语统计.xlsx'
           df.to_excel(save_path, index=False, encoding='utf-8')
        else:
            pass
        
if __name__ == "__main__":
    main()