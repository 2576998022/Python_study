"""
图书馆系统继承示例
演示类的继承和多态概念
"""

class LibraryItem:
    """图书馆物品基类"""
    
    def __init__(self, title: str, code: str):
        self.title = title          # 标题
        self.code = code            # 编号
        self._is_borrowed = False   # 借阅状态
    
    def borrow(self) -> bool:
        """借阅物品"""
        if self._is_borrowed:
            print(f"抱歉，{self.title}已被借出")
            return False
        self._is_borrowed = True
        print(f"成功借阅{self.title}")
        return True
    
    def return_item(self) -> None:
        """归还物品"""
        self._is_borrowed = False
        print(f"{self.title}已归还")
    
    def display_info(self) -> None:
        """显示信息（将被子类重写）"""
        pass

class Book(LibraryItem):
    """图书类（继承自LibraryItem）"""
    
    def __init__(self, title: str, author: str, code: str):
        super().__init__(title, code)  # 调用父类的初始化方法
        self.author = author           # 作者
    
    def display_info(self) -> None:
        """重写父类的显示信息方法"""
        print(f"图书：《{self.title}》")
        print(f"作者：{self.author}")
        print(f"编号：{self.code}")

class DVD(LibraryItem):
    """DVD类（继承自LibraryItem）"""
    
    def __init__(self, title: str, director: str, code: str):
        super().__init__(title, code)  # 调用父类的初始化方法
        self.director = director       # 导演
    
    def display_info(self) -> None:
        """重写父类的显示信息方法"""
        print(f"DVD：《{self.title}》")
        print(f"导演：{self.director}")
        print(f"编号：{self.code}")

def display_item_info(item: LibraryItem) -> None:
    """
    显示任何图书馆物品的信息
    这个函数展示了多态性
    """
    item.display_info()

# 使用示例
if __name__ == "__main__":
    # 创建不同的图书馆物品
    book = Book("Python入门", "张三", "B001")
    dvd = DVD("Python视频教程", "李四", "D001")
    
    # 使用多态显示信息
    print("=== 馆藏信息 ===")
    display_item_info(book)  # 显示图书信息
    print()
    display_item_info(dvd)   # 显示DVD信息 
    
    # 测试借还功能
    print("\n=== 借还测试 ===")
    book.borrow()      # 借书
    book.borrow()      # 尝试再次借同一本书
    book.return_item() # 还书
    book.borrow()      # 尝试再借同一本书