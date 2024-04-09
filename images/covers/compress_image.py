from PIL import Image
import os

def compress_image(infile, outfile, target_size_kb=500, quality_step=5):
    """压缩图片文件到目标大小。
    :param infile: 输入图片文件路径
    :param outfile: 输出图片文件路径
    :param target_size_kb: 目标大小，单位为KB
    :param quality: 初始压缩质量
    """

    target_size_bytes = target_size_kb * 1024  # 将KB转换为字节
    quality = 95  # 初始高质量

    # 加载图片
    img = Image.open(infile)
    # 尝试以不同的质量保存，直到达到目标大小或质量下限
    while quality >= 30:
        img.save(outfile, optimize=True, quality=quality)
        # 检查文件大小
        if os.path.getsize(outfile) <= target_size_bytes:
            print(f"压缩完成: 质量={quality}, 大小={os.path.getsize(outfile)} bytes")
            break
        quality -= quality_step
        if quality < 30:  # 如果质量低于5，结束循环
            print("已达到最低质量，但未达到目标大小")
            break

# 图片所在文件夹路径
input_folder = '.'

# 输出文件夹路径，这可以与输入文件夹相同，也可以是不同的文件夹
output_folder = '.' 
# output_folder = input_folder

# 目标文件大小（单位KB）
target_size_kb = 500

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        # 创建图片完整路径
        file_path = os.path.join(input_folder, filename)
        # 输出文件的完整路径
        out_file_path = os.path.join(output_folder, filename)
        # 压缩图片
        compress_image(file_path, out_file_path, target_size_kb=target_size_kb)

print("Images have been compressed.")


