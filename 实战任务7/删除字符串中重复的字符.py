# 开发人员    :  Yu
# 开发时间    : 2024/1/18  21:36
# 文件名称    : 删除字符串中重复的.PY
# 开发工具    : PyCharm
string1=input("请输入一个字符串: ")
newstr=list(set(string1))
newstr.sort(key=string1.index)
print(newstr)
print("".join(newstr))
