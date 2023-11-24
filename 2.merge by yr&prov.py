#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:33:37 2023

@author: petrichor
"""

import os

def merge_txt_files(input_folder, output_filename, file_prefix):
    
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    txt_files = [file for file in os.listdir(input_folder) if file.startswith(file_prefix) and file.endswith('.txt')]

    
    if not txt_files:
        print(f"No matching TXT files found in '{input_folder}' with the prefix '{file_prefix}'.")
        return

    # 合并文本内容
    merged_text = ""
    for txt_file in txt_files:
        txt_path = os.path.join(input_folder, txt_file)
        with open(txt_path, 'r', encoding='utf-8') as file:
            merged_text += file.read()

    # 写入合并的文本到输出文件
    output_path = os.path.join(input_folder, output_filename)
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(merged_text)

    print(f"Text files merged successfully. Merged content saved to '{output_path}'.")

# 指定输入文件夹、输出文件名和文件名前缀
input_folder = '/Users/petrichor/Desktop/SDA'
output_filename = 'mergedbyprov.txt'
file_prefix = '20'  # 替换文件名前缀

# 调用合并函数
merge_txt_files(input_folder, output_filename, file_prefix)