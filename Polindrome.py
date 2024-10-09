def isPalindrome(s: str) -> bool:
    s = s.lower()
    if len(s) == 1 or len(s) == 0:
        return True

    for el in s:
        if el.isalnum() != True:
            s = s.replace(el, '')

    if s == s[::-1]:
        return True
    else:
        return False