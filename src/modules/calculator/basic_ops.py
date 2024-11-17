"""基础运算模块"""

def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b

def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b

def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b

def divide(a: float, b: float) -> float:
    """
    除法运算
    如果除数为0，抛出ZeroDivisionError异常
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b 