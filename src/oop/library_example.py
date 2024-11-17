"""
图书馆借书系统示例
用生活场景解释面向对象编程的概念
"""

class Book:
    """图书类"""
    library_name = "城市图书馆"  # 类属性：所有书都属于这个图书馆
    
    def __init__(self, title: str, author: str):
        # 实例属性
        self.title = title      # 书名
        self.author = author    # 作者
        self._is_borrowed = False  # 私有属性：借阅状态
    
    @property
    def status(self) -> str:
        """获取图书状态"""
        return "已借出" if self._is_borrowed else "可借阅"
    
    def borrow(self) -> bool:
        """借书方法"""
        if self._is_borrowed:
            print(f"抱歉，《{self.title}》已被借出")
            return False
        self._is_borrowed = True
        print(f"成功借阅《{self.title}》")
        return True
    
    def return_book(self) -> None:
        """还书方法"""
        self._is_borrowed = False
        print(f"《{self.title}》已归还")

# 使用示例
if __name__ == "__main__":
    # 创建两本书
    book1 = Book("Python入门", "张三")
    book2 = Book("Python进阶", "李四")
    
    # 查看图书馆名称
    print(f"欢迎来到{Book.library_name}")
    
    # 查看图书状态
    print(f"《{book1.title}》状态：{book1.status}")
    
    # 借书
    book1.borrow()  # 第一次借书成功
    book1.borrow()  # 第二次借书失败
    
    # 还书
    book1.return_book()
    
    # 再次查看状态
    print(f"《{book1.title}》状态：{book1.status}") 