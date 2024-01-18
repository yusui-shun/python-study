# 开发人员    :  Yu
# 开发时间    : 2024/1/18  21:45
# 文件名称    : 7.5.PY
# 开发工具    : PyCharm
instr=input("请输入身份证信息：")
newstr=instr[6:10]+"年"+instr[10:12]+"月"+instr[12:14]+"日"
sexstr=int(instr[16])%2
sexstr=str(sexstr)
sexstr = sexstr.replace("0","女")
sexstr = sexstr.replace("1","男")
newstr =newstr+ sexstr
print(newstr)