def text(text):
    import re
    clean_string = re.sub('/[^a-zA-Z\s]+/', '', text).lower()
    string_list = clean_string.split(' ')
    list = {}
    for val in string_list:
        if val in list.keys():
            list[val] = list[val] + 1
        else:
            list.update({val: 1})
            
    sort_list = sorted(list.items(), key=lambda x: x[1], reverse=True)
    res_list = []
    for index, key in sort_list[:3]:
        res_list.append(index)
    return res_list
            
result = text("foo foo foo bar bar bar bar bar baz baz bus key key key key key key")
print(result)
