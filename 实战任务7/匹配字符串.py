# 开发人员    :  Yu
# 开发时间    : 2024/1/18  20:27
# 文件名称    : 匹配字符串.PY
# 开发工具    : PyCharm
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print('匹配值的起始位置: ',match.start())
print('匹配值的结束位置: ',match.end())
print('匹配位置的元组: ',match.span())
print('要匹配的字符串: ',match.string)
print('匹配数据: ',match.group())