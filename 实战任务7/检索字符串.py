# 开发人员    :  Yu
# 开发时间    : 2024/1/18  19:42
# 文件名称    : 检索字符串.PY
# 开发工具    : PyCharm
str1='@Python @扎克伯格 @雷军'
print('字符串',str1,'中包括',str1.count('@'),'个@符号')
print('字符串',str1,'中@符号首次出现的位置索引为：',str1.find('@'))
print('字符串',str1,'中@符号首次出现的位置索引为：',str1.index('@'))
print('字符串',str1,'中@符号首次出现的位置索引为：',str1.startswith('@'))
print('字符串',str1,'中@符号首次出现的位置索引为：',str1.endswith('@'))