"""
面向对象编程基础示例
演示类的基本概念和使用
"""

class Student:
    """学生类"""
    
    # 类属性
    school = "Python编程学校"
    
    # 构造方法
    def __init__(self, name: str, age: int):
        # 实例属性
        self.name = name
        self.age = age
        self._score = 0  # 私有属性，用下划线开头
    
    # 实例方法
    def study(self, course: str) -> None:
        """学习方法"""
        print(f"{self.name}正在学习{course}")
    
    # 属性访问器（getter）
    @property
    def score(self) -> int:
        return self._score
    
    # 属性修改器（setter）
    @score.setter
    def score(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在0-100之间")
        self._score = value

# 使用示例
if __name__ == "__main__":
    # 创建学生实例
    student = Student("小明", 18)
    
    # 访问属性
    print(f"学校：{Student.school}")
    print(f"姓名：{student.name}")
    
    # 调用方法
    student.study("Python")
    
    # 使用属性访问器和修改器
    student.score = 95  # 设置分数
    print(f"分数：{student.score}")  # 获取分数 