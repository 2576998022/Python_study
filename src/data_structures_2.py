# 字典(Dict)和集合(Set)的使用示例

def demonstrate_dict():
    """演示字典的基本操作"""
    print("=== 字典(Dict)的使用 ===")
    
    # 1. 创建字典
    # 字典使用花括号{}，包含键值对
    student = {
        "name": "小明",
        "age": 18,
        "scores": {"语文": 85, "数学": 92, "英语": 78}
    }
    
    # 2. 访问字典元素
    print("\n1. 访问字典元素：")
    print(f"学生姓名：{student['name']}")  # 使用键访问值
    print(f"数学成绩：{student['scores']['数学']}")  # 访问嵌套字典
    
    # 使用get方法安全访问（找不到键时返回默认值）
    print(f"物理成绩：{student.get('scores', {}).get('物理', '未参加考试')}")
    
    # 3. 修改和添加元素
    print("\n2. 修改和添加元素：")
    student['age'] = 19  # 修改已存在的值
    student['class'] = '高三二班'  # 添加新的键值对
    print(f"更新后的学生信息：{student}")

 
    
    # 4. 字典常用方法
    print("\n3. 字典常用方法：")
    print(f"所有键：{list(student.keys())}")  # 获取所有键
    print(f"所有值：{list(student.values())}")  # 获取所有值
    print(f"所有键值对：{list(student.items())}")  # 获取所有键值对
    
    # 删除元素
    removed_age = student.pop('age')  # 删除并返回值
    print(f"删除的年龄：{removed_age}")
    print(f"删除后的字典：{student}")

def demonstrate_set():
    """演示集合的基本操作"""
    print("\n=== 集合(Set)的使用 ===")
    
    # 1. 创建集合
    # 集合使用花括号{}，但只有值，没有键
    fruits = {"苹果", "香蕉", "橙子"}  # 直接创建
    numbers = set([1, 2, 2, 3, 3, 4])  # 从列表创建（会自动去重）
    
    # 2. 集合的特点
    print("\n1. 集合的特点：")
    print(f"原始数字列表：[1, 2, 2, 3, 3, 4]")
    print(f"转换为集合后：{numbers}")  # 自动去重
    
    # 3. 集合操作
    print("\n2. 集合操作：")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"并集：{set1 | set2}")  # 合并两个集合，去重
    print(f"交集：{set1 & set2}")  # 两个集合共有的元素
    print(f"差集：{set1 - set2}")  # 在set1中但不在set2中的元素
    
    # 4. 集合方法
    print("\n3. 集合方法：")
    fruits.add("葡萄")  # 添加元素
    print(f"添加后的水果集合：{fruits}")
    
    fruits.remove("香蕉")  # 删除元素
    print(f"删除后的水果集合：{fruits}")

def practice_exercise():
    """练习：使用字典和集合解决实际问题"""
    print("\n=== 练习：学生选课系统 ===")
    
    # 使用字典存储学生选课信息
    students = {
        "小明": {"语文", "数学", "英语"},
        "小红": {"数学", "英语", "物理"},
        "小华": {"语文", "英语", "化学"}
    }
    
    # 1. 查看所有可选课程（使用集合去重）
    all_courses = set()
    for courses in students.values():
        all_courses.update(courses)
    print(f"所有可选课程：{all_courses}")
    
    # 2. 查看同时选择了英语和数学的学生
    english_math_students = []
    for name, courses in students.items():
        if "英语" in courses and "数学" in courses:
            english_math_students.append(name)
    print(f"同时选择英语和数学的学生：{english_math_students}")
    
    # 3. 统计每门课程的选课人数
    # 创建一个空字典，用于存储每门课程的选课人数
    course_stats = {}

    # 遍历学生字典的所有值（每个值都是一个包含课程的集合）
    for courses in students.values():
        # 遍历每个学生选择的所有课程
        for course in courses:
            # 使用字典的get方法：
            # - 如果课程已存在，获取当前计数（默认值为0）
            # - 将计数加1
            # - 将新的计数更新到字典中
            # 例如：第一次遇到"语文"时，get返回0，加1后存储1
            #      第二次遇到"语文"时，get返回1，加1后存储2
            course_stats[course] = course_stats.get(course, 0) + 1

    # 打印统计结果
    print("\n课程选择统计：")
    # 遍历统计字典的所有键值对（课程名和选课人数）
    for course, count in course_stats.items():
        # 格式化打印每门课程的选课人数
        print(f"{course}: {count}人")

if __name__ == "__main__":
    # 演示字典的使用
    # demonstrate_dict()
    
    # # 演示集合的使用
    # demonstrate_set()
    
    # # 练习
    practice_exercise()
