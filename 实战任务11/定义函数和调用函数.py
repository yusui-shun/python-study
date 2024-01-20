def demo(obj):
    print("原值",obj)
    obj+=obj


#调用函数
print("============值传递======")
mot = "唯有被追赶的时候，你才能真正的奔跑"
print("函数调用前：",mot)
demo(mot)
print("函数被调用过后: ",mot)
print("=====引用传递=====")
list1=['邓肯','吉诺比利','帕克']
print("函数调用前: ",list1)
demo(list1)
print("函数被调用后： ",list1)
