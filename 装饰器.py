#Author:Win_Li   23147
#Date:2018-01-01 22:38

import time


flog = False

def flogger(flog):

    def show_time(tence):
        def add(*a):
            start_time = time.time()
            tence(*a)
            end_time = time.time()
            print('所用时间%d'%(start_time-end_time))

            if flog == True:
                print('已记录时间%d'%(start_time - end_time))
        return add
    return show_time

 # @flogger  #  add_01 = show_time(add_01)
def add_01(*a):
    sum = 0
    for i in a :
        sum += i
    time.sleep(3)
    print(sum)
add_01 = flogger(add_01)

add_01(4,2)


