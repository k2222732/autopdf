from PIL import Image
import os
from PyPDF2 import PdfMerger
import re

def numerical_sort(value):
    name_without_extend = f'{os.path.splitext(value)[0]}'
    numbers = re.findall(r'\d+', name_without_extend)
    return int(numbers[0]) if numbers else 0



def convert_images_to_pdf(folder_path, output_pdf_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print("指定的文件夹不存在")
        return

    # 初始化PDF合并器
    pdf_merger = PdfMerger()

    temp_pdf_paths = []
    
    #获取folder_path文件夹下的所有文件
    files = os.listdir(folder_path)
    #调用files.sort(key=numerical_sort)时, Python会自动取出files列表中的每个元素将它们作为参数传递给numerical_sort函数
    files.sort(key = numerical_sort)

    # 遍历文件夹中的所有文件
    for file in files:
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file)

        # 检查文件是否为图片
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            # 打开并转换图像
            with Image.open(file_path) as img:
                # 转换为RGB，防止RGBA问题
                img = img.convert('RGB')

                # os.path.splitext(file)这个函数将文件名分割为两部分：文件名和扩展名。
                temp_pdf_path = os.path.join(folder_path, f'{os.path.splitext(file)[0]}_temp.pdf')
                #.append()是Python中列表的一个内置方法，用于在列表的末尾添加一个新的元素。
                temp_pdf_paths.append(temp_pdf_path)
                img.save(temp_pdf_path)

                # 将PDF添加到合并器
                pdf_merger.append(temp_pdf_path)

    # 保存最终的PDF文件
    pdf_merger.write(output_pdf_path)
    pdf_merger.close()

    # 清理临时文件
    for temp_path in temp_pdf_paths:
        os.remove(temp_path)
    




# 使用函数
folder_path = '.\picture' # 替换为你的文件夹路径
output_pdf_path = '.\pdf\output.pdf' # 输出PDF的文件名
convert_images_to_pdf(folder_path, output_pdf_path)
