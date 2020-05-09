## 说明

1. 先初始化资源
2. 根据资源获得 汉字对应的4位数字编码词典

用法

```
hanzi_list,hanzi_num_dict = init_hanzi_resource()
number = "2306"
search_number2hanzi(hanzi_list,number)
name = "廾咔维瘩"
for n in name:
    print("汉字 %s 对应的数字是 %s "%(n,hanzi_num_dict[n]))

```