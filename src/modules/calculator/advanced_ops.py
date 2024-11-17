"""高级运算模块"""
import math

def power(base: float, exponent: float) -> float:
    """幂运算"""
    return math.pow(base, exponent)

def square_root(number: float) -> float:
    """平方根运算"""
    if number < 0:
        raise ValueError("不能对负数进行平方根运算")
    return math.sqrt(number)

def factorial(n: int) -> int:
    """阶乘运算"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("阶乘只能用于非负整数")
    if n == 0:
        return 1
    return n * factorial(n - 1) 