"""
函数类型注解示例
: str: 类型提示，表示这个参数应该是字符串类型
-> None: 返回值类型（如果有的话）
"""

# 1. 基本类型注解
def greet(name: str) -> str:
    return f"你好，{name}"

# 2. 多个参数的类型注解
def calculate_score(name: str, score: int, passed: bool) -> str:
    return f"{name}的分数是{score}，{'通过' if passed else '未通过'}"

# 3. 可选参数的类型注解
from typing import Optional
def get_user_info(name: str, age: Optional[int] = None) -> dict:
    info = {"name": name}
    if age is not None:
        info["age"] = age
    return info

# 4. 列表类型注解
from typing import List
def get_names(students: List[str]) -> List[str]:
    return [name.upper() for name in students]

# 5. 字典类型注解
from typing import Dict
def format_scores(scores: Dict[str, int]) -> str:
    return ", ".join(f"{name}: {score}" for name, score in scores.items())
