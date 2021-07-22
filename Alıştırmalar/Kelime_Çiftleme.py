def double_word(phrase, ref):
    str_list = phrase.split(' ')
    str_list.insert(ref - 1, str_list[ref - 1])
    for str in str_list:
        print(str, end=" ")
    return ''

str_var = "cat dog fish"

print(double_word(str_var,1))
print(double_word(str_var,2))
print(double_word(str_var,3))
