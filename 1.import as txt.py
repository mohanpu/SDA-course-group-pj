#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:31:27 2023

@author: petrichor
"""


import os
import PyPDF2

def extract_text_from_pdf(pdf_path, txt_path):
    # 打开PDF文件
    with open(pdf_path, 'rb') as pdf_file:
        # 创建PDF对象
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
       
        num_pages = pdf_reader.numPages

        # 打开TXT文件，准备写入文本
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            # 遍历每一页
            for page_num in range(num_pages):
              
                page = pdf_reader.getPage(page_num)
                
                # 提取文本
                text = page.extractText()

                # 写入文本到TXT文件
                txt_file.write(text)

def batch_extract_text_from_pdfs(pdf_folder, txt_folder):
  
    if not os.path.exists(txt_folder):
        os.makedirs(txt_folder)

    # 遍历PDF文件夹中的所有文件
    for pdf_filename in os.listdir(pdf_folder):
        if pdf_filename.endswith('.pdf'):
            # 构建PDF文件和TXT文件的完整路径
            pdf_path = os.path.join(pdf_folder, pdf_filename)
            txt_filename = pdf_filename.replace('.pdf', '.txt')
            txt_path = os.path.join(txt_folder, txt_filename)

            # 调用函数进行文本提取
            extract_text_from_pdf(pdf_path, txt_path)

# 指定PDF文件夹和TXT输出文件夹的路径
pdf_folder = '/Users/petrichor/Desktop/SDA'
txt_folder = '/Users/petrichor/Desktop/SDA'

# 调用批量提取函数
batch_extract_text_from_pdfs(pdf_folder, txt_folder)
