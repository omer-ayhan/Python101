shop_list = ["yağ", "un", "şeker"]
def shop_list_match(my_list, item):
    isMatch = False
    #checks if you entered list
    if isinstance(my_list, list):
        for i in my_list:
            # checks if the item matches. And when it happens it stops the loop
            if i is item:
                isMatch= True
                break
        # if nothing matches it will return assigned value which is False
        return isMatch
    else:
        print("you have to enter a list")
        return None

print(shop_list_match(shop_list, "yağ"))
print(shop_list_match(shop_list, "un"))
print(shop_list_match(shop_list, "şeker"))
print(shop_list_match(shop_list, "helva"))