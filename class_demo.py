# class SomeClassName:
#   # 构造函数，默认第一个参数被实例对象固定占用
#   def __init__(self, otherParams):
#       self.params = otherParams
#
#   # 定义方法，默认第一个参数被实例对象固定占用
#   def someMethodName(self):
#       # 执行逻辑

# 继承
# class SomeChildClassName(SomeClassName):
#   def __init__(self, otherParams):
#     super().__init__(otherParams)
#     # 子类自己的逻辑