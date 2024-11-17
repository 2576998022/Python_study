"""模块使用示例"""
from calculator import power, factorial
from calculator import add, subtract, multiply, divide

def main():
    # 基础运算示例
    print("=== 基础运算 ===")
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    
    # 高级运算示例
    print("\n=== 高级运算 ===")
    print(f"{a} 的 {b} 次方 = {power(a, b)}")
    print(f"{b} 的阶乘 = {factorial(b)}")

def lx():
    print("=== 模块使用示例 ===")
    a=3
    b=2
    print(f"{a} + {b} = {add(a,b)}")
    print(f"{a} - {b} = {subtract(a,b)}")
    print(f"{a} * {b} = {multiply(a,b)}")
    print(f"{a} / {b} = {divide(a,b):.1f}")
    print(f"{a}的{b}次方 = {power(a,b):.0f}")



if __name__ == "__main__":
    # main() 
    lx()