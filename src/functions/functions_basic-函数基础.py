"""
学习内容：Python函数基础
1. 函数定义和调用
2. 函数参数
   - 基本参数
   - 默认参数
   - 可变参数(*args)
   - 关键字参数(**kwargs)
3. 函数返回值
   - 单一返回值
   - 多个返回值
4. 函数文档字符串(docstring)
5. 函数作用域
"""

# 函数基础学习

# 1. 基本函数定义和调用
def greet(name):
    """
    简单的问候函数
    参数：
        name: 要问候的人名
    返回值：
        无
    """
    print(f"你好，{name}！")

# 2. 带返回值的函数
def calculate_sum(a, b):
    """
    计算两个数的和
    参数：
        a: 第一个数
        b: 第二个数
    返回值：
        两个数的和
    """
    return a + b

# 3. 默认参数
def greet_with_title(name, title="同学"):
    """
    带称谓的问候函数
    参数：
        name: 姓名
        title: 称谓，默认为"同学"
    """
    print(f"你好，{title} {name}！")

# 4. 多个返回值
def get_circle_info(radius):
    """
    计算圆的周长和面积
    参数：
        radius: 半径
    返回值：
        周长和面积的元组
    """
    import math
    circumference = 2 * math.pi * radius  # 周长
    area = math.pi * radius ** 2          # 面积
    return circumference, area

# 5. 可变参数
def calculate_average(*numbers):
    """
    计算任意数量数字的平均值
    参数：
        numbers: 任意数量的数字
    返回值：
        平均值，如果没有数字则返回0
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 6. 关键字参数
def create_student_info(**info):
    """
    创建学生信息字典
    参数：
        info: 包含学生信息的关键字参数
    返回值：
        学生信息字典
    """
    return info

def main():
    """主函数：演示各种函数的使用"""
    # 1. 基本函数调用
    print("1. 基本函数调用：")
    greet("小明")

    # 2. 带返回值的函数
    print("\n2. 带返回值的函数：")
    result = calculate_sum(5, 3)
    print(f"5 + 3 = {result}")

    # 3. 默认参数
    print("\n3. 默认参数：")
    greet_with_title("小红")  # 使用默认称谓
    greet_with_title("小李", "老师")  # 指定称谓

    # 4. 多个返回值
    print("\n4. 多个返回值：")
    radius = 5
    circ, area = get_circle_info(radius)
    print(f"半径为{radius}的圆：")
    print(f"周长：{circ:.2f}")
    print(f"面积：{area:.2f}")

    # 5. 可变参数
    print("\n5. 可变参数：")
    avg1 = calculate_average(1, 2, 3, 4, 5)
    print(f"平均值：{avg1}")
    numbers = [1, 2, 3, 4, 5]
    avg2 = calculate_average(*numbers)  # 解包列表
    print(f"使用列表解包的平均值：{avg2}")

    # 6. 关键字参数
    print("\n6. 关键字参数：")
    student = create_student_info(name="小明", age=18, grade="高一")
    print(f"学生信息：{student}")

if __name__ == "__main__":
    main() 