# 导入 math 模块用于获取圆周率
import math
import math

def calculate_circumference(radius):
    """计算圆的周长"""
    return 2 * math.pi * radius

def calculate_area(radius):
    """计算圆的面积"""
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = float(input("请输入圆的半径: "))
    print(f"周长: {calculate_circumference(r):.2f}")
    print(f"面积: {calculate_area(r):.2f}")
# 获取用户输入的半径
try:
    radius = float(input("请输入球的半径: "))
    
    # 计算球的体积
    volume= 4/3 * math.pi * radius ** 3
    
    
    # 输出结果
    print(f"球的体积是: {volume:.2f}")
except ValueError:
    print("输入无效，请输入一个有效的数字。")
    