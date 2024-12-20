def format_student_info(**info):
    """格式化学生信息"""
    default_info = {
        'name': '未知',
        'age': 0,
        'grade': '未知',
        'score': 0
    }
    
    default_info.update(info)
    
    return f"""学生姓名: {default_info['name']}
年龄: {default_info['age']}
年级: {default_info['grade']}
分数: {default_info['score']}"""

def combined_example(*args, **kwargs):
    """同时使用*args和**kwargs"""
    print(f"位置参数: {args}")
    print(f"关键字参数: {kwargs}")

# 调用示例
# print(format_student_info(name="小明", age=18),"\n")
# print(format_student_info(name="小红", score=95, grade="高一"))
combined_example(1, 2, 3, name="小明", age=18)
