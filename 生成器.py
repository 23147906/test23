#Author:Win_Li   23147
#Date:2018-01-02 22:56

# def f(n):
#     return n**3
#
# # a = [x*2  for x in range(10) ]   #列表生成式
# # print(a)
#
# a = [f(x)  for x in range(10)]   #列表生成式
# print(a)
# print(type(a))

# a = (x*2  for x in range(10) ) #生成器：将列表生成器的中括号换成小括号。
# print(a)      # <generator object <genexpr> at 0x00000179E81CA2B0>
#
# # print(next(a))   #等价于 a.__next() in py2: a.next()
# # print(next(a))   #逐个生成,每次生成一个。
# #生成器就是一个可迭代对象（iterable)
#
# for i in a:  #py 回收机制，逐个产生，新的对应时，旧的回收。
#     print(i)

# def foo():
#     print('ok')
#     yield 1
#
#     print('OK2')
#     yield 2
#
# g = foo()
# print(g)  #<generator object foo at 0x0000013457B6A2B0>
#
# # next(g)
# # next(g)
#
# for i in g :
#     print(i)


# def bar():
#     print('ok1')
#     count = yield 1
#     print(count)
#
#     print('ok2')
#     yield 2
#
# b = bar()
#
# b.send(None)
#  next(b) 第一次send 前如果没有next,之鞥传一个send（None)
#  因为第一次send 不知道给谁传值
# ret=b.send('eee')
# #   send() 将value传给了yield前的变量。
# print(ret)

# def foo():
#     print('ok1')
#     yield 1
#
#     print('ok2')
#     yield 2
#
# g = foo()
# print(g)
# next(g) # 到yield 1 结束
# next(g) # 从yield 1 开始


def fibo(max):
    n,before,after = 0,0,1
    while n < max:
        yield after
        before,after = after,before+after
        n = n + 1


num = input('请输入你要计算的值：')
num1 =int(num)
g = fibo(num1)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))








