dict_data={
    '0':'O',
    '1':'I',
    '2':'Z',
    '3':'E',
    '4':'Y',
    '5':'S',
    '6':'G',
    '7':'L',
    '8':'B',
    '9':'P'
}
def translate_code_word(word):
    #转化字符串
    result=[]
    global dict_data
    for i in word:
        result.append(dict_data[i])
    return result

word=input('请输入暗语：')
while True:
        result_list=translate_code_word(word)
        result_string="".join(result_list)
        print('转换后是：%s'%result_string)
        if result_string == 'BYE':
            break
        word = input('请输入暗语:')