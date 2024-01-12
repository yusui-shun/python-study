# 开发人员    :  Yu
# 开发时间    : 2024/1/12  11:51
# 文件名称    : 计算BMI.PY
# 开发工具    : PyCharm
height=1.78
print("您的身高："+str(height))
weight=69.3
print("您的体重："+str(weight))
bmi=weight/(height*height)
print("您的BMI指数为："+str(bmi))
if bmi<18.5:
    print("您的体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("正常范围，注意保持")
if bmi>=24.9 and bmi<29.9:
    print("您的体重过重")
if bmi>=24.9:
    print("肥胖")