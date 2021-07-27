def remove_duplicates(num_list):
    try:
        # the reason we return with the 'list()' function because 'set()' function returns its value as an object
        return list(set(num_list))
    except:
        print("please add a list")

print(remove_duplicates(["a","a","a"]))
print(remove_duplicates([2, 2, 1]))