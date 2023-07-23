def unpacking_of_lst(lst_2):
    while True:
        new_lst = []
        for i in lst_2:
            if type(i) is list:
                new_lst.extend(i)
            else:
                new_lst.append(i)
        lst_2 = new_lst
        if any(map(lambda x: type(x) is list, new_lst)) is False:   # It seemed easier for me to make a check for a cycle stop here
            break                                                   # Yes, i am strange or stupid... :)
    return lst_2
