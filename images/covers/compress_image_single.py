from PIL import Image
import os

# 图片所在文件夹路径
input_folder = '.'

# 输出文件夹路径，如果要原地转换，则与输入文件夹相同
output_folder = input_folder

# 图片质量，范围从1（最差）到95（最好）。高质量意味着更少的压缩
quality = 95

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('virtualenv.png')):
        # 创建图片完整路径
        file_path = os.path.join(input_folder, filename)
        # 打开图片
        img = Image.open(file_path)
        # 保存图片，调整质量参数进行压缩
        img.save(os.path.join(output_folder, 'co_' + filename), quality=quality)

print("Images have been compressed.")

