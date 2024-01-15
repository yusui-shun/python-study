# 开发人员    :  Yu
# 开发时间    : 2024/1/15  16:29
# 文件名称    : 6.3.PY
# 开发工具    : PyCharm
list=[]
for i in range(5):
    a=input("请输入商品编号和商品名称进行商品入库，每次只能输入一件商品:\n")
    list.append(a)
for item in list:
    print(item)
num1=input("请输入要购买的商品的编号\n")
for j in range(5):
    goods = str(list[j])
    num2=goods.find(num1)
    if num2 != -1:
        print("您购物车里已经选择的商品为:\n",list[j])