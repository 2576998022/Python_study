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