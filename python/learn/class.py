#!/usr/bin/python3
 
class Site:
  def __init__(self, name, url):
    self.name = name            # public
    self.__url = url            # private
  def who(self):
    print('name  : ', self.name)
    print('url : ', self.__url)
  def __foo(self):              # 私有方法
    print('这是私有方法')
  def foo(self):                # 公共方法
    print('这是公共方法')
    self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
x.foo()      # 报错

#!/usr/bin/python3
 
class Vector:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def __str__(self):
    return 'Vector (%d, %d)' % (self.a, self.b)
  def __add__(self, other):
    return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print (v1 + v2)