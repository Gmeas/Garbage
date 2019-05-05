"""
import sys
"""
"""
迭代器有两种基本方法：
iter()和next()
迭代器只能前进不能后退
"""
"""
list=[1,2,3,4]
it=iter(list)           #创建迭代器对象
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for a in list:
    print(a,end=" ")
print(" ")

b=iter(list)
for a in b:
    print(a,end=" ")
print()

list1=list
it1=iter(list1)
while True:
    try:
        print(next(it1))
    except StopIteration:
        sys.exit()
"""

class MyNumbers:            #python的构造函数是_init_()
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)




