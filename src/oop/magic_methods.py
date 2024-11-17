"""
特殊方法（魔术方法）示例
演示Python类中常用的特殊方法
"""

class Book:
    """图书类，展示常用的特殊方法"""
    
    def __init__(self, title: str, author: str, price: float):
        """初始化方法"""
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self) -> str:
        """字符串表示，用于print()"""
        return f"《{self.title}》 by {self.author}"
    
    def __repr__(self) -> str:
        """开发者字符串表示"""
        return f'Book("{self.title}", "{self.author}", {self.price})'
    
    def __eq__(self, other) -> bool:
        """相等性比较"""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other) -> bool:
        """小于比较，用于排序"""
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price
    
    def __len__(self) -> int:
        """返回长度（这里返回书名长度）"""
        return len(self.title)
    
    def __getitem__(self, key: str):
        """使对象可以像字典一样访问"""
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "price":
            return self.price
        raise KeyError(f"'{key}' 不是有效的键")

# 使用示例
if __name__ == "__main__":
    # 创建两本书
    book1 = Book("Python入门", "张三", 59.9)
    book2 = Book("Python进阶", "李四", 89.9)
    book3 = Book("Python入门", "张三", 59.9)  # 与book1相同的书
    
    # 1. __str__ 和 __repr__ 的使用
    print("\n=== 字符串表示 ===")
    print(f"普通字符串: {book1}")        # 使用 __str__
    print(f"开发者表示: {repr(book1)}")  # 使用 __repr__
    
    # 2. __eq__ 的使用
    print("\n=== 相等性比较 ===")
    print(f"book1 == book2: {book1 == book2}")  # False
    print(f"book1 == book3: {book1 == book3}")  # True
    
    # 3. __lt__ 的使用
    print("\n=== 排序 ===")
    books = [book1, book2]
    for book in sorted(books):  # 按价格排序
        print(f"{book.title}: ￥{book.price}")
    
    # 4. __len__ 的使用
    print("\n=== 长度 ===")
    print(f"书名长度: {len(book1)}")
    
    # 5. __getitem__ 的使用
    print("\n=== 字典式访问 ===")
    print(f"作者: {book1['author']}")
    print(f"价格: {book1['price']}") 