# 导入 pandas 库，用来处理数据
import pandas as pd
# 导入 matplotlib.pyplot 库，用来画图
import matplotlib.pyplot as plt

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    
    这个函数会创建一个表格，里面有学生的名字、年龄、成绩和所在城市，
    然后把这个表格保存成一个文件。
    
    Returns:
        None
    """
    # 创建一个字典，就像一个小本子，用来记录数据
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '陈七'],  # 学生的名字
        '年龄': [25, 30, None, 22, 28],  # 学生的年龄，None 表示没有数据
        '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],  # 学生的成绩
        '城市': ['北京', '上海', '广州', '深圳', '上海']  # 学生所在的城市
    }

    # 把字典转换成一个表格（DataFrame）
    df = pd.DataFrame(data)

    # 把表格保存成一个文件，文件名是 'data/data.csv'
    df.to_csv('data/data.csv', index=False, encoding='utf-8')
    print("数据已保存到 data/data.csv 文件中。")


def load_data():
    """
    任务1: 读取数据文件
    
    这个函数会从文件中读取刚才保存的表格。
    
    Returns:
        pd.DataFrame: 返回读取的表格
    """
    try:
        # 从文件 'data/data.csv' 中读取表格
        data = pd.read_csv('data/data.csv')
        print("数据加载成功！")
        return data
    except FileNotFoundError:
        # 如果文件没有找到，就提示用户先创建文件
        print("数据文件未找到，请先运行 creat_frame() 函数生成数据文件。")
        return None


def show_basic_info(data):
    """
    任务2: 显示数据基本信息
    
    这个函数会显示表格的一些基本信息，比如每一列都有什么数据。
    """
    print("数据基本信息：")
    print(data.info())  # 打印表格的基本信息
    print("\n数据的前几行：")
    print(data.head())  # 打印表格的前几行数据


def handle_missing_values(data):
    """
    任务3: 处理缺失值
    
    这个函数会找到表格里没有数据的地方，然后用合适的方法填补它们。
    
    Args:
        data (pd.DataFrame): 输入的表格
    
    Returns:
        pd.DataFrame: 处理后的表格
    """
    print("处理缺失值前：")
    print(data.isnull().sum())  # 打印每一列缺失数据的数量

    # 找到表格里所有的数字列
    numeric_columns = data.select_dtypes(include=['number']).columns
    # 对于每一列数字，如果发现有缺失值，就用这一列的平均数来填补
    for col in numeric_columns:
        data[col].fillna(data[col].mean(), inplace=True)

    print("\n处理缺失值后：")
    print(data.isnull().sum())  # 再次打印缺失数据的数量
    return data


def analyze_statistics(data):
    """
    任务4: 统计分析数值列
    
    这个函数会计算表格里数字列的一些统计信息，比如平均数、中位数和标准差。
    
    Args:
        data (pd.DataFrame): 输入的表格
    """
    print("数值列的统计分析结果：")
    # 找到表格里所有的数字列
    numeric_columns = data.select_dtypes(include=['number']).columns
    # 对于每一列数字，计算它的平均数、中位数和标准差
    for col in numeric_columns:
        mean_value = data[col].mean()  # 平均数
        median_value = data[col].median()  # 中位数
        std_value = data[col].std()  # 标准差
        print(f"\n{col} 列的统计信息：")
        print(f"均值: {mean_value}")
        print(f"中位数: {median_value}")
        print(f"标准差: {std_value}")


def visualize_data(data, column_name='成绩'):
    """
    任务6: 数据可视化
    
    这个函数会用画图的方式展示表格里的数据。
    
    Args:
        data (pd.DataFrame): 输入的表格
        column_name (str, optional): 要画图的列名，默认是 '成绩'
    """
    print(f"绘制 {column_name} 的直方图：")
    # 用 pandas 的画图功能，画出指定列的直方图
    data[column_name].plot.hist(bins=10, edgecolor='black')
    plt.title(f'{column_name} 分布')  # 设置标题
    plt.xlabel(column_name)  # 设置 x 轴标签
    plt.ylabel('频数')  # 设置 y 轴标签
    plt.show()  # 显示图表


def save_processed_data(data):
    """
    任务7: 保存处理后的数据
    
    这个函数会把处理后的表格保存成一个新的文件。
    
    Args:
        data (pd.DataFrame): 处理后的表格
    """
    data.to_csv('data/processed_data.csv', index=False)
    print("处理后的数据已保存到 data/processed_data.csv 文件中。")


def main():
    """
    主函数，执行所有数据处理流程
    
    这个函数会按照顺序执行上面定义的所有任务。
    """
    # 创建数据文件（如果尚未创建）
    creat_frame()

    # 1. 读取数据
    data = load_data()
    if data is None:
        return  # 如果数据加载失败，就退出程序

    # 2. 显示基本信息
    show_basic_info(data)

    # 3. 处理缺失值
    processed_data = handle_missing_values(data.copy())

    # 4. 统计分析
    analyze_statistics(processed_data)

    # 5. 数据可视化
    visualize_data(processed_data)

    # 6. 保存处理后的数据
    save_processed_data(processed_data)


if __name__ == "__main__":
    main()  # 运行主函数
