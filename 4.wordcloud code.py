#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 00:19:54 2023

@author: black
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取 Excel 文件
excel_file = '甘肃高频词语统计处理版.xlsx'  # 将文件名替换为你的 Excel 文件名
df = pd.read_excel(excel_file)

# 提取词语和频率列
words = df.iloc[:, 0].tolist()  # 提取第一列数据作为词语列表
frequencies = df.iloc[:, 1].tolist()  # 提取第二列数据作为频率列表

# 将词语和频率转换成字典形式
word_freq = {words[i]: frequencies[i] for i in range(len(words))}

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'

# 创建一个 WordCloud 对象并指定字体参数
wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# 显示词云图
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()