[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/dqIrOmgD)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19088765)
# 计算物理实验第七周练习

## 目录结构

```
cp2025-practice-week7/
├── data/                   # 实验数据文件
│   ├── bwCat.tif           # 图像平均实验数据
│   └── stressFibers.txt    # 图像特征强调实验数据
├── docs/                   # 项目说明文档
│   ├── pandas数据操作练习.md
│   ├── SymPy绘图.md
│   ├── 电偶极子电势与电场计算与可视化.md
│   ├── 图像平均.md
│   └── 图像特征强调.md
├── results/                # 实验结果与报告，需要学生完成
│   ├── pandas数据操作练习实验报告.md
│   ├── SymPy绘图实验报告.md
│   ├── 电偶极子电势与电场的计算与可视化实验报告.md
│   ├── 图像平均实验报告.md
│   └── 图像特征强调实验报告.md
├── solutions/              # 参考答案，请勿修改
│   ├── electric_field_solution.py
│   ├── image_average_solution.py
│   ├── image_feature_emphasis_solution.py
│   ├── pandas_practice_solution.py
│   └── SymPy_plot_solution.py
├── src/                    # 源代码需要学生完成
│   ├── electric_field.py
│   ├── image_average.py
│   ├── image_feature_emphasis.py
│   ├── pandas_practice.py
│   └── SymPy_plot.py
├── tests/                  # 测试代码, 请勿修改
│   ├── test_electric_field.py
│   ├── test_image_average.py
│   ├── test_image_feature_emphasis.py
│   ├── test_pandas_practice.py
│   └── test_Sympy_plot.py
└── README.md               # 项目说明文件
```

## 作业内容

本次实验包含五个独立的练习项目，每个项目都有对应的文档说明、代码模板和测试文件。

### 1. 图像平均处理
- **目标**：实现不同尺寸的平均滤波器，分析滤波器尺寸对图像平滑效果的影响
- **文件**：`src/image_average.py`
- **测试**：`tests/test_image_average.py`
- **说明文档**：`docs/图像平均.md`

### 2. 图像特征强调
- **目标**：构建高斯-拉普拉斯组合滤波器，实现不同方向的特征检测
- **文件**：`src/image_feature_emphasis.py`
- **测试**：`tests/test_image_feature_emphasis.py`
- **说明文档**：`docs/图像特征强调.md`

### 3. Pandas数据操作练习
- **目标**：掌握Pandas库的基本操作，进行数据分析与可视化
- **文件**：`src/pandas_practice.py`
- **测试**：`tests/test_pandas_practice.py`
- **说明文档**：`docs/pandas数据操作练习.md`

### 4. SymPy绘图
- **目标**：使用SymPy进行符号计算与函数绘图
- **文件**：`src/SymPy_plot.py`
- **测试**：`tests/test_Sympy_plot.py`
- **说明文档**：`docs/SymPy绘图.md`

### 5. 电偶极子电势与电场计算与可视化
- **目标**：计算电偶极子的电势分布，可视化电场线和等势面
- **文件**：`src/electric_field.py`
- **测试**：`tests/test_electric_field.py`
- **说明文档**：`docs/电偶极子电势与电场计算与可视化.md`

## 完成要求

1. 阅读各项目的说明文档，理解实验原理和要求
2. 完成`src/`目录下对应的代码文件
3. 运行测试确保代码正确性：`python -m unittest tests/test_项目名.py`
4. 在`results/`目录下完成对应的实验报告

## 提交方式

将完成的代码和实验报告提交到github，确保：
- 所有代码能够通过测试
- 实验报告包含完整的分析和结论
- 不要修改`tests/`目录下的测试代码

## 评分标准
每个实验模块占总分的五分之一，总分为50分。评分将通过自动测试完成，测试通过即得满分。

## 参考资料
《Python物理建模初学者指南》第八章