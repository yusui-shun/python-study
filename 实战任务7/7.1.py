import  re
string = '2018 Amazon Jeff Bezos 1120'
print("(1)",string[5:])
print("(1)",string.replace("2018","").strip())
newlist=list(filter(str.isdigit,string))
print("(2)","".join(newlist))
print("(2)",string[0:4]+string[23:27])
print("(3)",string("2018",str(int("2018")*2)).replace("1120",str(int("1120")*2)))
print("(5)",string.replace("2018","4036").replace("1120","2240"))
print("(5)",str(int(string[0:4]*2)+string[4:23]+str(int(string[23:27])*2)))