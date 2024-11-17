"""
学习内容：Python模块开发
1. 模块的创建和使用
2. 函数的封装
3. 常量定义
4. 模块测试代码
5. __name__变量的使用
6. 数学运算函数实现
   - 加减乘除
   - 异常处理
"""

def add(a, b):
    """加法函数"""
    return a + b

def subtract(a, b):
    """减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

def divide(a, b):
    """
    除法函数
    如果除数为0，返回None
    """
    if b == 0:
        return None
    return a / b

# 定义一些常量
PI = 3.14159
E = 2.71828

# 如果直接运行这个模块，执行测试代码
if __name__ == "__main__":
    # 测试代码
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}") 