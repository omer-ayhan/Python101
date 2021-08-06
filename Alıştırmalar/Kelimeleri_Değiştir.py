def switch_words(string):
    str_list = string.split(' ')
    # str_list.reverse()
    if len(str_list)>2:
        return "You can't write more than two words"
    else:
        return str_list[-1] + ' ' + str_list[-2]

print(switch_words("Golden Bear"))
print(switch_words("day snow"))