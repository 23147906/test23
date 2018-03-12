# -*- UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-08 23:48


from multiprocessing import Process
import time


def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = Process(target=f, args=('win', )) # 创建进程对象
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()

    print('end!')

