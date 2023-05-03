def plusOne(digits):
    #return_list is the list we are gonna return once we append everything
    return_list = []

    #converts digits to a string, then joins them, then converts them to integers, then adds.
    str_list = list(map(str, digits))
    i = ''.join(str_list)
    i_int = int(i)
    i_added = i_int + 1
    i_str = str(i_added)
    
    #now appends every number in there as a single element
    for i in i_str:
        return_list.append(i)
    int_return_list = list(map(int, return_list))

    return int_return_list

    """
    :type digits: List[int]
    :rtype: List[int]
    """

print(plusOne([1,2,3]))