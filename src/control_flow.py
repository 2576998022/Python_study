# 1. if条件判断：根据年龄判断人生阶段
def check_age(age):
    """
    根据输入的年龄判断人生阶段
    参数：
        age: 年龄，整数类型
    """
    # 先判断是否是负数
    if age < 0:
        print("年龄不能为负数！")
    # 再判断是否未成年（小于18岁）
    elif age < 18:
        print("你还是未成年人")
    # 接着判断是否是青年（18-35岁）
    elif age < 35:
        print("你正值青年")
    # 其他情况（35岁及以上）
    else:
        print("你已经成年了")

# 2. for循环：展示三种常见的for循环用法
def demonstrate_for():
    """演示三种常见的for循环使用方式"""
    
    # 示例1：使用range()生成数字序列进行循环
    # range(3)生成0,1,2三个数字
    print("\n1. 基础for循环：")
    for i in range(3):  # i会依次取值0,1,2
        print(f"这是第{i+1}次循环")  # i+1转换为人类习惯的从1开始计数
    
    # 示例2：直接遍历列表元素
    print("\n2. 遍历列表：")
    fruits = ["苹果", "香蕉", "橙子"]  # 创建一个水果列表
    for fruit in fruits:  # fruit将依次取列表中的每个值
        print(f"我喜欢吃{fruit}")
    
    # 示例3：使用enumerate同时获取索引和元素
    print("\n3. 带索引的遍历：")
    for index, fruit in enumerate(fruits):  # enumerate返回索引和值的对
        print(f"第{index+1}个水果是{fruit}")

# 2.1 for循环：遍历字典
def demonstrate_for_dict():
    """演示遍历字典的两种常见方式"""
    # 创建一个字典
    student_scores = {"张三": 85, "李四": 90, "王五": 78}
    # 遍历字典的键值对
    for name, score in student_scores.items():
        print(f"{name}的成绩是{score}")  # 打印键值对


# 3. while循环：展示基础用法和猜数字游戏
def demonstrate_while():
    """演示while循环的两种常见使用场景"""
    
    # 示例1：使用计数器的while循环
    print("\n1. 基础while循环：")
    count = 0  # 初始化计数器
    while count < 3:  # 当计数器小于3时继续循环
        print(f"count的值是{count}")
        count += 1  # 计数器加1
    
    # 示例2：实现简单的猜数字游戏
    print("\n2. while循环猜数字：")
    target = 5  # 设置目标数字
    while True:  # 无限循环，直到猜对为止
        guess = int(input("猜一个1-10的数字："))  # 获取用户输入
        if guess == target:
            print("恭喜你猜对了！")
            break  # 猜对了，跳出循环
        elif guess < target:
            print("猜小了")
        else:
            print("猜大了")

# 4. break和continue：展示循环控制语句
def demonstrate_break_continue():
    """演示break和continue在循环中的使用"""
    
    # 示例1：break用法 - 提前结束循环
    print("\n1. break的使用：")
    for i in range(5):  # 本应循环0-4
        if i == 3:  # 当i等于3时
            print("遇到3，提前结束循环")
            break  # 直接结束整个循环
        print(f"当前数字是{i}")
    
    # 示例2：continue用法 - 跳过当前循环
    print("\n2. continue的使用：")
    for i in range(5):  # 循环0-4
        if i == 3:  # 当i等于3时
            print("跳过3")
            continue  # 跳过本次循环，继续下一次
        print(f"当前数字是{i}")

# 程序入口
if __name__ == "__main__":
    # 测试所有函数
    # 1. 测试年龄判断
    print("===测试if条件判断===")
    check_age(15)  # 测试未成年
    check_age(25)  # 测试青年
    check_age(40)  # 测试成年
    
    # 2. 测试for循环的三种用法
    print("\n===测试for循环===")
    demonstrate_for()
    
    # 2.1 测试遍历字典
    print("\n===测试遍历字典===")
    demonstrate_for_dict()
    
    # 3. 测试while循环
    print("\n===测试while循环===")
    demonstrate_while()
    
    # 4. 测试break和continue
    print("\n===测试break和continue===")
    demonstrate_break_continue()