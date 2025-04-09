import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():

    stressFibers =np.loadtxt('stressFibers.txt')
    return stressFibers


def create_gauss_filter():
    """
    创建高斯滤波器

    返回:
        numpy.ndarray: 51x51的高斯滤波器矩阵

    说明:
        - 滤波器尺寸为51x51(-25到25)
        - X方向标准差σ_x=√5, Y方向标准差σ_y=√45
        - 公式: exp(-0.5*(X²/5 + Y²/45))
    """
    v = np.arange(-25, 26)  # 创建-25到25的坐标范围
    X, Y = np.meshgrid(v, v)  # 生成网格坐标
    gauss_filter = np.exp(-0.5 * (X ** 2 / 5 + Y ** 2 / 45))  # 计算高斯函数值
    return gauss_filter


def create_combined_filter(gauss_filter):
    """
    创建高斯-拉普拉斯组合滤波器

    参数:
        gauss_filter: 高斯滤波器矩阵

    返回:
        numpy.ndarray: 组合后的滤波器矩阵

    说明:
        - 使用3x3拉普拉斯滤波器与高斯滤波器卷积
        - 拉普拉斯核: [[0,-1,0],[-1,4,-1],[0,-1,0]]
    """
    laplace_filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])  # 定义拉普拉斯算子
    combined_filter = sim.convolve(gauss_filter, laplace_filter, mode='constant')  # 卷积运算
    return combined_filter


def plot_filter_surface(filter, title):
    """
    绘制滤波器3D表面图

    参数:
        filter: 要绘制的滤波器矩阵
        title: 图形标题(使用英文)

    说明:
        - 使用mpl_toolkits.mplot3d绘制3D表面
        - 图形尺寸设置为10x6英寸
    """
    fig = plt.figure(figsize=(10, 6))  # 创建图形窗口
    ax = fig.add_subplot(111, projection='3d')  # 添加3D子图

    v = np.arange(-25, 26)
    X, Y = np.meshgrid(v, v)  # 创建网格坐标

    # 绘制3D表面
    surf = ax.plot_surface(X, Y, filter, cmap='viridis',
                           linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)  # 添加颜色条
    ax.set_title(title)  # 设置标题
    plt.show()  # 显示图形


def process_and_display(stressFibers, filter, vmax_ratio=0.5):
    """
    处理图像并显示结果

    参数:
        stressFibers: 输入图像数据
        filter: 要应用的滤波器
        vmax_ratio: 显示时的最大强度比例(默认0.5)

    返回:
        numpy.ndarray: 处理后的图像数据
    """
    # 应用滤波器
    processed = sim.convolve(stressFibers, filter, mode='constant')

    # 显示处理结果
    plt.figure(figsize=(8, 6))
    img = plt.imshow(processed, cmap='gray',
                     vmin=0, vmax=vmax_ratio * processed.max())
    plt.colorbar(img, fraction=0.046, pad=0.04)  # 添加颜色条
    plt.title('滤波后的图像')  # 设置中文标题
    plt.show()

    return processed


def main():
    """
    主函数，执行完整的图像特征强调流程

    流程:
    1. 加载应力纤维数据
    2. 创建并可视化高斯滤波器
    3. 创建并可视化组合滤波器
    4. 应用不同方向的滤波器处理图像
    5. 显示处理结果
    """
    # 1. 加载数据
    stressFibers = load_stress_fibers()

    # 2. 任务(a): 创建并显示高斯滤波器
    print("创建高斯滤波器...")
    gauss_filter = create_gauss_filter()

    # 显示高斯滤波器2D视图
    plt.figure(figsize=(8, 6))
    plt.imshow(gauss_filter, cmap='viridis')
    plt.colorbar()
    plt.title('高斯滤波器(2D视图)')
    plt.show()

    # 显示高斯滤波器3D视图
    plot_filter_surface(gauss_filter, 'Gauss Filter 3D')

    # 3. 任务(b): 创建组合滤波器
    print("创建组合滤波器...")
    combined_filter = create_combined_filter(gauss_filter)

    # 显示组合滤波器2D视图
    plt.figure(figsize=(8, 6))
    plt.imshow(combined_filter, cmap='viridis', origin='lower')
    plt.colorbar()
    plt.title('组合滤波器(2D视图)')
    plt.show()

    # 显示组合滤波器3D视图
    plot_filter_surface(combined_filter, 'Combined filter 3D')

    # 4. 任务(c): 应用垂直滤波器
    print("使用垂直滤波器处理图像...")
    combined1 = process_and_display(stressFibers, combined_filter, 0.5)

    # 5. 任务(d): 应用水平滤波器
    print("使用水平滤波器处理图像...")
    combined_filter2 = sim.rotate(combined_filter, angle=90, reshape=False)
    combined2 = process_and_display(stressFibers, combined_filter2, 0.4)

    # 可选: 45度方向滤波器
    print("使用45度方向滤波器处理图像...")
    combined_filter3 = sim.rotate(combined_filter, angle=45, reshape=False)
    combined3 = process_and_display(stressFibers, combined_filter3, 0.3)


if __name__ == "__main__":
    main()
