def is_pangram(sentence):
    list = []
    exeptions = [' ','_', '.', ',', '"', "'",'-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    list_abc = []
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for x in abc:
        list_abc.append(x)
    list_abc = set(list_abc)
    for x in sentence:
        if x in exeptions:
            continue
        else:
            list.append(x.lower())
    list = set(list)
    if list == list_abc:
        return True
    else:
        return False
