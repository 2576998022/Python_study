def print_info():
    """打印个人信息的函数"""
    age = 18
    print(f"我的年龄是{age}")

    name = "lee"
    print(f"我的名字是{name}")

    height = 1.69
    print(f"我的身高是{height}")

    is_student = True
    print(f"我是一个学生吗？{is_student}")

# 简单的运算：

a =5
b =6

def calculator():
    print(f"加法{a}+{b}={a+b}")

    print(f"减法{a}-{b}={a-b}")

    print(f"乘法{a}*{b}={a*b}")

    print(f"除法{a}/{b}={a/b :.1f}")

    print(f"取余{a}%{b}={a%b}")

    print(f"幂运算{a}**{b}={a**b}")

    print(f"取整除{a}//{b}={a//b}")

if __name__ == "__main__":
    calculator()
    print("\n")
    print_info()
