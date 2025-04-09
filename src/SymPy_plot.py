"""
SymPy 绘图练习模板

本模板包含三个绘图练习，分别演示：
1. 基本函数绘图
2. 隐函数绘图 
3. 参数曲面绘图

学生需要完成每个函数中的TODO部分来实现相应绘图功能。
"""

import sympy as sp
from sympy.plotting import plot, plot_implicit, plot3d_parametric_surface

def problem1():
    """
    绘制函数 cos(tan(pi*x)) 的图像
    
    要求：
    - 使用 sympy.plotting.plot 函数
    - 绘制区间为 [-1, 1]
    - 添加适当的坐标轴标签和标题
    
    返回:
        None (直接显示绘图窗口)
    """
    # 定义符号变量 x
    x = sp.Symbol('x')
    # 定义要绘制的表达式
    expr = sp.cos(sp.tan(sp.pi * x))
    # 完成绘图函数调用
    plot(expr, (x, -1, 1), xlabel='x', ylabel='y', title='Plot of cos(tan(pi*x))')


def problem2():
    """
    绘制隐函数 e^y + cos(x)/x + y = 0 的图像
    
    要求:
    - 使用 sympy.plotting.plot_implicit 函数
    - 选择合适的绘图区间避免除零错误(x不能为0)
    - 添加适当的坐标轴标签和标题
    - 设置足够的采样点(points参数)以获得平滑曲线
    
    返回:
        None (直接显示绘图窗口)
    """
   # 定义符号变量x,y
    x, y = sp.symbols('x,y')
    # 定义隐函数表达式
    implicit_expr = sp.exp(y) + sp.cos(x) / x + y
    # 完成隐函数绘图
    plot_implicit(implicit_expr, (x, -10, 10), (y, -10, 10), xlabel='x', ylabel='y', title='Plot of e^y + cos(x)/x + y = 0', points=500)


def problem3():
    """
    绘制三维参数曲面
    
    参数曲面定义:
    x = exp(-s)*cos(t)
    y = exp(-s)*sin(t) 
    z = t
    
    要求:
    - 使用 sympy.plotting.plot3d_parametric_surface 函数
    - 设置 s 的范围为 [0, 8]
    - 设置 t 的范围为 [0, 5*pi]
    - 添加适当的坐标轴标签和标题
    
    返回:
        None (直接显示绘图窗口)
    """
   # 定义符号变量 s,t
    s, t = sp.symbols('s,t')
    # 定义参数方程
    x = sp.exp(-s) * sp.cos(t)
    y = sp.exp(-s) * sp.sin(t)
    z = t
    # 完成三维参数曲面绘图
    plot3d_parametric_surface(x, y, z, (s, 0, 8), (t, 0, 5 * sp.pi), xlabel='x', ylabel='y', zlabel='z', title='3D Parametric Surface Plot')


if __name__ == "__main__":
    # 依次运行三个问题的绘图函数
    problem1()
    problem2()
    problem3()
