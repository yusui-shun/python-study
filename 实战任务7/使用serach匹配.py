# 开发人员    :  Yu
# 开发时间    : 2024/1/18  20:34
# 文件名称    : 使用serach匹配.PY
# 开发工具    : PyCharm
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.search(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern,string,re.I)
print(match)
