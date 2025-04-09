import numpy as np  # 导入numpy库，用于数值计算
import scipy.ndimage as sim  # 导入scipy.ndimage库，用于图像处理
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot库，用于图像显示

def create_small_filter():
    """
    创建一个3×3的平均滤波器。

    返回:
        numpy.ndarray: 3×3的滤波器矩阵，每个元素值为1/9。
    """
    # 创建一个3×3的数组，每个元素初始化为1/9
    # 这个滤波器也被称为"盒式滤波器"，用于图像平滑处理
    # 1/9的值确保滤波器的总和为1，从而保持图像的亮度不变
    return np.ones((3, 3)) / 9

def create_large_filter():
    """
    创建一个15×15的平均滤波器。

    返回:
        numpy.ndarray: 15×15的滤波器矩阵，每个元素值为1/225。
    """
    # 创建一个15×15的数组，每个元素初始化为1/225
    # 15×15滤波器比3×3滤波器更大，会生成更平滑的效果
    # 1/225的值确保滤波器的总和为1，从而保持图像的亮度不变
    return np.ones((15, 15)) / (15 * 15)

def process_image(input_file):
    """
    处理图像并显示原始图像和滤波后的结果。

    参数:
        input_file (str): 输入图像文件路径。

    功能:
        1. 读取输入图像。
        2. 创建3×3和15×15平均滤波器。
        3. 对图像应用两种滤波器。
        4. 显示原始图像和两种滤波结果对比。
    """
    # 1. 读取图像 - 使用matplotlib的imread()函数
    # imread()函数会根据文件类型自动处理图像
    # 对于.tif文件，它会正确读取为numpy数组
    img = plt.imread(input_file)

    # 2. 创建滤波器 - 调用已实现的函数
    small_filter = create_small_filter()  # 创建3×3滤波器
    large_filter = create_large_filter()  # 创建15×15滤波器

    # 3. 应用卷积 - 使用scipy.ndimage的convolve()函数
    # convolve()函数执行图像与滤波器的卷积操作
    # mode='reflect'参数处理图像边界，使用镜像反射
    # 这里我们使用默认的mode参数，因为它在大多数情况下工作良好
    small_result = sim.convolve(img, small_filter)
    large_result = sim.convolve(img, large_filter)

    # 4. 显示结果 - 使用matplotlib绘制对比图
    # 创建一个15英寸宽、5英寸高的画布
    plt.figure(figsize=(15, 5))

    # 显示原始图像
    plt.subplot(1, 3, 1)  # 创建1行3列的第1个子图
    plt.imshow(img, cmap='gray')  # 使用灰度图显示
    plt.title('Original Image')  # 设置标题
    plt.axis('off')  # 关闭坐标轴

    # 显示3×3滤波结果
    plt.subplot(1, 3, 2)  # 创建1行3列的第2个子图
    plt.imshow(small_result, cmap='gray')  # 使用灰度图显示
    plt.title('3×3 Filter Result')  # 设置标题
    plt.axis('off')  # 关闭坐标轴

    # 显示15×15滤波结果
    plt.subplot(1, 3, 3)  # 创建1行3列的第3个子图
    plt.imshow(large_result, cmap='gray')  # 使用灰度图显示
    plt.title('15×15 Filter Result')  # 设置标题
    plt.axis('off')  # 关闭坐标轴

    # 调整布局并显示
    plt.tight_layout()  # 自动调整子图参数
    plt.show()  # 显示图像

if __name__ == "__main__":
    # 主程序入口
    # 确保data/bwCat.tif文件存在
    # 如果文件不存在，请从Nelson, PMLS Datasets下载并放置在正确的位置
    process_image('data/bwCat.tif')
