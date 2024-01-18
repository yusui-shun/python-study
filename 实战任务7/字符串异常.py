# 开发人员    :  Yu
# 开发时间    : 2024/1/18  19:35
# 文件名称    : 字符串异常.PY
# 开发工具    : PyCharm
str1= '人生苦短，我用Python'
try:
    substr1=str1[15]
except IndexError:
    print('指定的索引不存在')
