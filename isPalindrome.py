def isPalindrome(x):
    p = str(x)
    palindrome = p[::-1]
    if palindrome == p:
        return True
    else:
        return False

print(isPalindrome(10))