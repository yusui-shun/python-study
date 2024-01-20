import os
phonedic={}
choice = 9
isfind=0
print("""STAR通讯录功能：  1：添加联系人  2：删除联系人  3：查找联系人  4：电话本显示：

""")
if os.path.isfile("phonedic.txt"):
    if os.path.getsize("phonedic.txt"):
        file=open("phonedic.txt",'r')
        for line in file:
            line.strip()
            if len(line)>6:
                liststr=line.split(",")



