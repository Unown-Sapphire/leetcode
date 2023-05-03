#imma take this as a W but idk wtf a ListNode is so yeah

def addTwoNumbers(l1, l2):
    return_list = []

    #l1 list definition
    l1_2 = l1[::-1]
    l1_3 = map(str, l1_2)
    l1_4 = ''.join(l1_3)
    
    #l2 list definition
    l2_2 = l2[::-1]
    l2_3 = map(str, l2_2)
    l2_4 = ''.join(l2_3)
    
    #math starts here
    return_value = int(l1_4) + int(l2_4)
    for i in str(return_value):
        return_list.append(i)
    new_return_list1 = return_list[::-1]
    new_return_list2 = list(map(int, new_return_list1))
    return new_return_list2

print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))