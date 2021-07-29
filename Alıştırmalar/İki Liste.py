def two_list(list1, list2):
    new_dict = dict()
    try:
        # checks if length of two lists are equal 
        if len(list1)!=len(list2):
            raise IndexError
        for key in list1:
            # adds two lists as key-value pair
            new_dict[key] = list2[list1.index(key)]
        return new_dict
    except TypeError:
        return "Please enter all as a list"
    except IndexError:
        return "lists have to be in same length"
    except:
        return "an error occured"

l1 = [1,2,3]
l2 = [4,5,6]
print(two_list(l1, l2))