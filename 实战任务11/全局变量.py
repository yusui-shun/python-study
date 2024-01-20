message= '唯有被追赶的时候，你才能真正地奔跑'
print('函数体外： 全局变量message =',message)
def f_demo():
    message = '命运给与我们的不是失望之路，而是机会之杯'
    print('函数体内：全局变量message = ',message)
f_demo()
print('函数体外： 全局变量message =',message)

message= '唯有被追赶的时候，你才能真正地奔跑'
print('函数体外： 全局变量message =',message)
def f_demo1():
    global message
    message = '命运给与我们的不是失望之路，而是机会之杯'
    print('函数体内：全局变量message = ',message)
f_demo1()
print('函数体外： 全局变量message =',message)