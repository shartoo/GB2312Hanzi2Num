def init_hanzi_resource(resource_file="./hanzi_gb2312"):
    '''
        https://www.qqxiuzi.cn/zh/hanzi-gb2312-bianma.php
        根据资源表 整理成列表形式
    :param resource_file:
    :return:
    '''
    result = {}
    # 汉字对应的GB2312编码数字
    hanzi_num_dict = {}
    index = 0
    word_index = 0
    with open(resource_file,"r",encoding="utf-8") as rd:
        lines = rd.readlines()
        tmp_result = []
        for line in lines:
             line = line.replace("\n","")
             clean_line = line.replace(" ","")
             #print(clean_line)
             if not clean_line.isdigit():
                 if len(str(clean_line).strip())!=0:
                    line = line[2:]
                    hanzis = line.split(" ")
                    for hanzi in hanzis:
                        # 从第10行开始时汉字了
                        if index>9:
                            hanzi = eval("u"+"\'"+str(hanzi).strip()+"\'")
                        tmp_result.append(hanzi)
                        zone_id = str(index)
                        word_id = str(word_index)
                        if len(str(index))==1:
                            zone_id = "0"+zone_id
                        if len(str(word_id))==1:
                            word_id = "0" +word_id
                        hanzi_num_dict[hanzi] = zone_id+word_id
                        # 一个区 可能跨越多行，区中汉字的序号要连续
                        word_index = word_index + 1
                 else:
                    key = str(index)
                    if len(key)==1:
                        key = "0"+key
                    result[key]=tmp_result
                    tmp_result= []
             else:
                #print("读取到数字行了\t",clean_line)
                index = clean_line[:2]
                if index.startswith("0"):
                    index = index[1:]
                index = int(index)
                word_index = 0
    return result,hanzi_num_dict

def search_number2hanzi(hanzi_list,number):
    '''
        根据编码数字查询对应的汉字
    :param hanzi_list: 87行GB2312汉字列表，每一行包含94个汉字   https://www.qqxiuzi.cn/zh/hanzi-gb2312-bianma.php
    :param number:
    :return:
    '''

    head =str(number)[:2]
    tail = str(number)[2:]
    if (tail.startswith("0")):
        tail = tail[1:]
    hanzi = hanzi_list[head][int(tail)]
    print("数字 %s 对应的汉字是 %s "%(str(number),hanzi))

