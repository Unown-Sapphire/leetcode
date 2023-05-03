def anagram(a, b):
    word1_list = []
    word2_list = []
    word1 = a.upper()
    word2 = b.upper()

    for i in word1:
        word1_list.append(i)
    for n in word2:
        word2_list.append(n)
    
    word1_list.sort()
    word2_list.sort()

    if word1_list == word2_list:
        return True
    else:
        return False

print(anagram("knee", "keen"))  