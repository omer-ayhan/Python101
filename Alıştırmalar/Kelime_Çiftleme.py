def double_word(phrase, ref):
    new_str = ''
    str_list = phrase.split(' ')
    str_list.insert(ref - 1, str_list[ref - 1])
    for str in str_list:
        new_str+=str + ' '
    return new_str.strip()

str_var = "cat dog fish"

print(double_word(str_var,1))
print(double_word(str_var,2))
print(double_word(str_var,3))
