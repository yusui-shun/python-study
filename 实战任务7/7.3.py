# 开发人员    :  Yu
# 开发时间    : 2024/1/18  21:27
# 文件名称    : 7.3.PY
# 开发工具    : PyCharm
template1="%06d\t"
template2="%.2f"
id =0
# 商品信息
instr=input("请输入商品信息:")
newlist=instr.split(" ")
while "" in newlist:
    newlist.remove("")
price = int(newlist[2])
id = id + 1
print(template1 % id + "   "+ newlist[0]+"   "+ newlist[1] + "   "+ chr(65509)+template2%price)
instr=input("请输入输入商品信息")
newlist=instr.split("")