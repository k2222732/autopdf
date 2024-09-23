import os
from PyPDF2 import PdfMerger
import re

def numerical_sort(value):
    name_without_extend = f'{os.path.splitext(value)[0]}'
    numbers = re.findall(r'\d+', name_without_extend)
    return int(numbers[0]) if numbers else 0

def merge_pdfs(folder_path, output_pdf_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print("指定的文件夹不存在")
        return

    # 初始化PDF合并器
    pdf_merger = PdfMerger()

    # 获取文件夹下所有文件
    files = os.listdir(folder_path)
    
    # 调用files.sort(key=numerical_sort)时，Python会根据文件名中的数字进行排序
    files.sort(key=numerical_sort)

    # 遍历文件夹中的所有文件
    for file in files:
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file)

        # 检查文件是否为PDF文件
        if file.lower().endswith('.pdf'):
            # 将PDF添加到合并器
            with open(file_path, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)

    # 保存合并后的PDF文件
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)
    
    pdf_merger.close()

# 使用函数
folder_path = '.\\inputpdfs'  # 替换为你的文件夹路径
output_pdf_path = '.\\outputpdf\\merged_output.pdf'  # 输出合并后的PDF文件名
merge_pdfs(folder_path, output_pdf_path)