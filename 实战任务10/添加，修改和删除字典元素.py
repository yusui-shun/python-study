dictionary=dict((('邓肯','石佛'),('吉诺比利','妖刀'),('帕克','跑车')))
dictionary["罗宾逊"]="海军上将"
print(dictionary)
dictionary["帕克"]="法国跑车"
print(dictionary)
del dictionary["帕克"]
print(dictionary)
if "帕克" in dictionary:
    del dictionary["帕克"]
print(dictionary)