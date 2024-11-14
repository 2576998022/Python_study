# 数据结构基础：列表(List)和元组(Tuple)的使用示例

def demonstrate_list():
    """演示列表的基本操作"""
    print("=== 列表(List)的使用 ===")
    
    # 1. 创建列表
    fruits = ["苹果", "香蕉", "橙子"]  # 使用方括号创建列表
    numbers = [1, 2, 3, 4, 5]  # 数字列表
    mixed = ["Python", 3.14, True, [1, 2]]  # 混合类型列表
    
    # 2. 访问列表元素
    print("\n1. 访问列表元素：")
    print(f"第一个水果是：{fruits[0]}")  # 使用索引访问，从0开始
    print(f"最后一个水果是：{fruits[-1]}")  # 负索引从末尾开始
    print(f"前两个水果是：{fruits[:2]}")  # 切片操作
    
    # 3. 修改列表
    print("\n2. 修改列表：")
    fruits[1] = "葡萄"  # 修改单个元素
    print(f"修改后的水果列表：{fruits}")
    
    # 4. 列表常用方法
    print("\n3. 列表常用方法：")
    fruits.append("芒果")  # 在末尾添加元素
    print(f"添加后的列表：{fruits}")
    
    fruits.insert(1, "香蕉")  # 在指定位置插入元素
    print(f"插入后的列表：{fruits}")
    
    removed_fruit = fruits.pop()  # 删除并返回最后一个元素
    print(f"删除的水果是：{removed_fruit}")
    print(f"删除后的列表：{fruits}")
    
    fruits.remove("香蕉")  # 删除指定元素
    print(f"删除香蕉后的列表：{fruits}")
    
    # 5. 列表操作
    print("\n4. 列表操作：")
    print(f"列表长度：{len(fruits)}")  # 获取列表长度
    print(f"苹果在列表中的位置：{fruits.index('苹果')}")  # 查找元素位置
    
    fruits.sort()  # 排序列表
    print(f"排序后的列表：{fruits}")
    
    fruits.reverse()  # 反转列表
    print(f"反转后的列表：{fruits}")

def demonstrate_tuple():
    """演示元组的基本操作"""
    print("\n=== 元组(Tuple)的使用 ===")
    
    # 1. 创建元组
    coordinates = (10, 20)  # 使用圆括号创建元组
    point3d = (1, 2, 3)
    single_item = (1,)  # 单个元素的元组需要加逗号
    
    # 2. 访问元组元素
    print("\n1. 访问元组元素：")
    print(f"x坐标：{coordinates[0]}")
    print(f"y坐标：{coordinates[1]}")
    
    # 3. 元组的特点
    print("\n2. 元组的特点：")
    # coordinates[0] = 30  # 这行会报错，因为元组是不可变的
    print(f"元组长度：{len(coordinates)}")
    print(f"2在point3d中的位置：{point3d.index(2)}")
    print(f"1在point3d中出现的次数：{point3d.count(1)}")
    
    # 4. 元组的应用
    print("\n3. 元组的应用：")
    # 多变量赋值
    x, y = coordinates  # 元组解包
    print(f"x = {x}, y = {y}")
    
    # 函数返回多个值
    def get_point():
        return (100, 200)
    
    point_x, point_y = get_point()
    print(f"获取的坐标：x = {point_x}, y = {point_y}")

def practice_exercise():
    """练习：综合运用列表和元组"""
    print("\n=== 练习：学生成绩管理 ===")
    
    # 使用列表存储学生成绩（可修改）
    scores = [85, 92, 78, 90, 88]
    print(f"所有成绩：{scores}",end="\n")
    print(f"最高分：{max(scores)}",end="\n")
    print(f"最低分：{min(scores)}",end="\n")
    print(f"平均分：{sum(scores) / len(scores):.2f}",end="\n")

    
    # 使用元组存储科目信息（不可修改）
    subjects = ("语文", "数学", "英语", "物理", "化学")
    print(f"\n所有科目：{subjects}")
    
    # 将科目和成绩对应起来
    for subject, score in zip(subjects, scores): # zip函数将两个列表合并成一个由元组组成的列表
        print(f"{subject}: {score}分")

    print(list(zip(subjects, scores))) # 打印合并后的列表

if __name__ == "__main__":
    # 演示列表的使用
    demonstrate_list()
    
    # 演示元组的使用
    demonstrate_tuple()
    
    # 练习
    practice_exercise() 