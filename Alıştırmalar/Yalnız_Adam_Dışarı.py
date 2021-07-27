def Yalnız_adam_dışarı(num_people, num_groups):
        while True:
            if num_groups>0 and num_groups<=num_people:
                num_groups -= 1
                num_people -= 2
                if num_people==-1:
                    return 1
            else: break
        return num_people
print(Yalnız_adam_dışarı(20,7)) # 6
print(Yalnız_adam_dışarı(100,10)) # 80
print(Yalnız_adam_dışarı(17,10)) # 1
print(Yalnız_adam_dışarı(17,5)) # 7
print(Yalnız_adam_dışarı(4,2)) # 1
# 10 17
# 9 15
# 8 13
# 7 11
# 6 9
# 5 7
# 4 5
# 3 3
# 2 1
