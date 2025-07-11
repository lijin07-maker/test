# 导入 math 模块用于获取圆周率
import math

# 获取用户输入的半径
try:
    radius = float(input("请输入球的半径: "))
    
    # 计算球的体积
    volume= 4/3 * math.pi * radius ** 3
    
    
    # 输出结果
    print(f"球的体积是: {volume:.2f}")
except ValueError:
    print("输入无效，请输入一个有效的数字。")
    