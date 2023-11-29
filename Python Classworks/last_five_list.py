lst1 = [1, 2, 3, 2, 6, 7, 9, 1]
lst2 = [8, 9,10]

def get_last_five(lst):
    if len(lst) < 5:
        return "Too short"
    else:
        return lst[-5:]
    
print(get_last_five(lst1))
print(get_last_five(lst2))

