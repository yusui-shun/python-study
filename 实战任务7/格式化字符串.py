# 开发人员    :  Yu
# 开发时间    : 2024/1/18  20:07
# 文件名称    : 格式化字符串.PY
# 开发工具    : PyCharm
template='编号: {:0>9s}\t公司名称: {:s} \t 官网: http://www.{:s}.com'
context1=template.format('7','百度','baidu')
context2=template.format('8','重邮','cqupt')
print(context1)
print(context2)