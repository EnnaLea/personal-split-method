def mysplit(strng):
    list_string = []
    new_str = ""
    for i in range(len(strng)):
        if strng[i] != " " and strng[i] != ",":
            new_str += strng[i]
        else:
            if new_str:
                list_string.append(new_str)
            new_str = ""
    if new_str:
        list_string.append(new_str)
    return list_string

# print(len(mysplit("To be or not to be, that is the question")))
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))