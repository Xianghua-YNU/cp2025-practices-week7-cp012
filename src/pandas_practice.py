# 导入 pandas 库，用来处理数据
import pandas as pd
# 导入 matplotlib.pyplot 库，用来画图
import matplotlib.pyplot as plt

def creat_frame():
    """
    创建一个包含学生信息的表格并保存为CSV文件。
    
    这个函数会创建一个表格，里面有学生的名字、年龄、成绩和所在城市，
    然后把这个表格保存成一个文件。
    
    Returns:
        None
    """
    # 创建一个字典，就像一个小本子，用来记录数据
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '陈七'],  # 学生的名字
        '年龄': [25, 30, None, 22, 28],  # 学生的年龄，None 表示没有数据
        '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],  # 学生成绩
        '城市': ['北京', '上海', '广州', '深圳', '上海']  # 学生所在的城市
    }

    # 把字典转换成一个表格（DataFrame），表格可以方便地处理数据
    df = pd.DataFrame(data)

    # 把表格保存成一个文件，文件名是 'data/data.csv'
    # index=False 表示不保存表格的索引列
    # encoding='utf-8' 表示用 UTF-8 编码保存文件，这样可以正确保存中文
    df.to_csv('data/data.csv', index=False, encoding='utf-8')
    print("数据已保存到 data/data.csv 文件中。")


def load_data():
    """
    任务1: 读取数据文件
    
    这个函数会从文件中读取刚才保存的表格。
    
    Returns:
        pd.DataFrame: 返回读取的表格
    """
    # 从文件 'data/data.csv' 中读取表格
    # pd.read_csv 是 pandas 提供的一个函数，用来读取 CSV 文件
    return pd.read_csv('data/data.csv')


def show_basic_info(data):
    """
    任务2: 显示数据基本信息
    
    这个函数会显示表格的一些基本信息，比如每一列都有什么数据。
    """
    print("数据基本信息：")
    # data.info() 是 pandas 提供的一个方法，用来显示表格的基本信息
    data.info()
    print("\n数据的前几行：")
    # data.head() 是 pandas 提供的一个方法，用来显示表格的前几行数据
    print(data.head())


def handle_missing_values(data):
    """
    任务3: 处理缺失值
    
    这个函数会找到表格里没有数据的地方，然后用合适的方法填补它们。
    
    Args:
        data (pd.DataFrame): 输入的表格
    
    Returns:
        pd.DataFrame: 处理后的表格
    """
    # 找到表格里所有包含缺失值的列
    missing_columns = data.columns[data.isnull().any()].tolist()
    # 遍历每一列缺失值的列
    for col in missing_columns:
        # 检查这一列是否是数字类型
        if pd.api.types.is_numeric_dtype(data[col]):
            # 如果是数字类型，用这一列的平均值填补缺失值
            data[col] = data[col].fillna(data[col].mean())
    # 返回处理后的表格
    return data


def analyze_statistics(data):
    """
    任务4: 统计分析数值列
    
    这个函数会计算表格里数字列的一些统计信息，比如平均数、中位数和标准差。
    
    Args:
        data (pd.DataFrame): 输入的表格
    """
    # 找到表格里所有的数字列
    numeric_columns = data.select_dtypes(include=['number']).columns
    # 遍历每一列数字列
    for col in numeric_columns:
        # 计算这一列的平均值
        mean_value = data[col].mean()
        # 计算这一列的中位数
        median_value = data[col].median()
        # 计算这一列的标准差
        std_value = data[col].std()
        # 打印统计信息
        print(f"{col} 列的均值: {mean_value}, 中位数: {median_value}, 标准差: {std_value}")


def visualize_data(data, column_name='成绩'):
    """
    任务5: 数据可视化
    
    这个函数会用画图的方式展示表格里的数据。
    
    Args:
        data (pd.DataFrame): 输入的表格
        column_name (str, optional): 要画图的列名，默认是 '成绩'
    """
    # 用 pandas 的 plot 方法画出指定列的直方图
    data[column_name].plot.hist()
    # 显示图表
    plt.show()


def save_processed_data(data):
    """
    任务6: 保存处理后的数据
    
    这个函数会把处理后的表格保存成一个新的文件。
    
    Args:
        data (pd.DataFrame): 处理后的表格
    """
    # 把表格保存成一个新的文件，文件名是 'processed_data.csv'
    data.to_csv('processed_data.csv', index=False)
    print("处理后的数据已保存到 processed_data.csv 文件中。")


def main():
    """
    主函数，执行所有数据处理流程
    
    这个函数会按照顺序执行上面定义的所有任务。
    """
    # 1. 读取数据
    data = load_data()
    
    # 2. 显示基本信息
    show_basic_info(data)
    
    # 3. 处理缺失值
    # data.copy() 是为了创建数据的一个副本，避免修改原始数据
    processed_data = handle_missing_values(data.copy())
    
    # 4. 统计分析
    analyze_statistics(processed_data)
    
    # 5. 数据可视化
    visualize_data(processed_data)
    
    # 6. 保存处理后的数据
    save_processed_data(processed_data)


if __name__ == "__main__":
    # 运行主函数，开始执行程序
    main()
