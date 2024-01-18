# 开发人员    :  Yu
# 开发时间    : 2024/1/18  20:46
# 文件名称    : 正则表达式匹配ip.PY
# 开发工具    : PyCharm
import re
pattern=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1='127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
for item in match:
    print(item[0])
