# 开发人员    :  Yu
# 开发时间    : 2024/1/15  16:07
# 文件名称    : 6.1.PY
# 开发工具    : PyCharm
year=[89,98,00,75,68,37,58,90]
print("当前序列：",year)
for index,value in enumerate(year):
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
year.sort()
print(year)