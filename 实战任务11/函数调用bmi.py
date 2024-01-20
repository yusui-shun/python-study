def fun_bmi(person,height,weight):
    '''
    功能：根据身高体重计算BMI指数
    :param person:姓名
    :param height: 身高 米
    :param weight: 体重 kg
    :return: BMI
    '''
    print(person+"的身高"+str(height)+"米\t体重："+str(weight)+"千克")
    bmi=weight/(height*height)
    print(person+"的BMI指数为： "+str(bmi))
    if bmi<18.5:
        print("您的体重过轻")
    if bmi>=18.5 and bmi<24.9:
        print("正常范围，注意保持")
    if bmi>=24.9 and bmi<29.9:
        print("您的体重过重")
    if bmi>=29.9:
        print("肥胖s")
        
fun_bmi("匿名",1.78,67)