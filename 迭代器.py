#Author:Win_Li   23147
#Date:2018-01-03 23:03


l = [1,2,4,6]
d = iter(l)
print(d)  #<list_iterator object at 0x000001DAB8FBDE48>

print(next(d))

#for 循环内部三件事：
#1.调用可迭代对象的iter（）方法返回一个迭代器对象
#2.不断调用迭代器对象的next（）方法
#3.处理StopIteration
for i in [1,2,3,5]:
    iter([1,2,3,5])