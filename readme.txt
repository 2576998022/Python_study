# Python学习计划 (适合零基础初学者)

## 学习目标
通过系统化的学习，使零基础学员掌握Python基础知识，为后续进行接口自动化测试打下坚实基础。

## 学习阶段

### 第一阶段：Python基础入门（2-3周）
1. Python环境搭建
   - Python安装
   - IDE选择（推荐PyCharm社区版）
   - 第一个Python程序：Hello World

2. Python基础语法
   - 变量和数据类型（整数、浮点数、字符串、布尔值）
   - 注释的使用
   - print() 函数使用
   - 基本运算符（+、-、*、/、%）

3. 程序控制流
   - if条件判断
   - for循环
   - while循环
   - break和continue语句

### 第二阶段：数据结构基础（2-3周）
1. 基本数据结构
   - 列表（List）的使用
   - 元组（Tuple）的使用
   - 字典（Dict）的使用
   - 集合（Set）的使用

2. 字符串操作
   - 字符串的基本操作
   - 字符串格式化
   - 常用字符串方法

### 第三阶段：函数和模块（2周）
1. 函数基础
   - 函数的定义和调用
   - 参数传递
   - 返回值
   - 变量作用域

2. 模块使用
   - 导入模块
   - 常用内置模块
   - 第三方模块的安装和使用

### 第四阶段：文件操作和异常处理（2周）
1. 文件操作
   - 文件的读写
   - 文件路径处理
   - CSV文件处理

2. 异常处理
   - try-except语句
   - 常见异常类型
   - 异常处理最佳实践

## 学习建议
1. 每天保持1-2小时的学习时间
2. 多动手练习，不要只看不练
3. 每学完一个知识点，都要做相应的练习
4. 遇到问题先尝试自己解决，实在解决不了再寻求帮助
5. 建立学习笔记的好习惯

## 学习资源推荐
1. 在线教程：
   - 菜鸟教程 Python 基础：https://www.runoob.com/python3/python3-tutorial.html
   - 廖雪峰 Python 教程：https://www.liaoxuefeng.com/wiki/1016959663602400

2. 练习平台：
   - LeetCode（编程题目练习）：https://leetcode.cn/
   - 实验楼（在线编程环境）：https://www.lanqiao.cn/

## 阶段性检验
每个阶段结束后，都应该能完成相应的小项目，比如：
1. 第一阶段：实现简单的计算器程序
2. 第二阶段：实现学生信息管理系统
3. 第三阶段：实现文件批量重命名工具
4. 第四阶段：实现简单的日志分析器

# VS Code 开发环境配置说明

## 终端配置
- VS Code 默认终端已设置为 Windows 命令提示符(CMD)
- 配置方式：
  1. 通过界面：命令面板 -> "Terminal: Select Default Profile" -> 选择 "Command Prompt"
  2. 通过 settings.json：设置 "terminal.integrated.defaultProfile.windows": "Command Prompt"

配置完成后，每次新建终端时都会默认打开 CMD，而不是其他终端类型。 

## cursor开发环境配置

### 插件配置
1. 必装插件：
   - Code Runner：代码快速运行
   - Python：Python语言支持
   - Pylance：Python语言服务器
   - Python Extension Pack：Python扩展包

### Code Runner配置
1. 基本设置：
   - 运行在集成终端
   - 自动保存文件
   - 运行前清除之前的输出
   - 支持中文输出
   
2. 快捷键：
   - 运行代码：Ctrl+Alt+N
   - 停止运行：Ctrl+Alt+M

### 使用建议
1. 始终在虚拟环境中开发
2. 使用Code Runner运行代码前确保文件已保存
3. 如遇到中文乱码，检查终端编码设置

### Python代码执行顺序
1. 代码执行顺序
   - Python代码从上到下顺序执行
   - 函数定义时不会执行函数内容
   - 函数只有在被调用时才会执行

2. 函数的使用
   - 使用def定义函数
   - 函数内的代码需要缩进
   - 函数在被调用时执行

3. if __name__ == "__main__"的使用
   - 用于控制代码的执行
   - 区分直接运行和被导入的情况
   - 是Python的常用idiom