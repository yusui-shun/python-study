dictionary={'key1':'value','key2':'value2','key3':'value3','keyn':'valuen'}
print(dictionary)
dictionary1={'qq':'84978981','YU':'1526892925','无语':'17358334939'}
print(dictionary1)
dictionary2={}
dictionary3=dict()
name = ['邓肯','吉诺比利','帕克']
sign = ['石佛','妖刀','跑车']
dictionary4=dict(zip(name,sign))
print(dictionary4)
dictionary5=dict(邓肯='石佛',吉诺比利='妖刀',帕克='跑车')
print(dictionary5)
name_list=['邓肯','吉诺比利','帕克']
dictionary6=dict.fromkeys(name_list)
print(dictionary6)
name_tuple=('邓肯','吉诺比利','帕克')
dict2={name_tuple:sign}
print(dict2)
print(dictionary4['吉诺比利'])
print("吉诺比利的错号是:",dictionary4.get('吉诺比利'))
print("罗宾逊的绰号是:",dictionary4.get('罗宾逊','我的字典里没有此人'))