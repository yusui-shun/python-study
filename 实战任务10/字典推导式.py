import random
randomdict = {i:random.randint(10,100) for i in range(1,5)}
print("生成的字典为:",randomdict)
mr = set(['零基础学Java','零基础学Android','零基础学C语言','零基础学C#','零基础学PHP'])
mr.remove('零基础学Java')
print('使用remove()方法移除指定元素后: ',mr)
mr.pop()
print('使用pop()方法移除一个元素后：',mr)
mr.clear()
print('使用clear()方法清空集合后: ',mr)
