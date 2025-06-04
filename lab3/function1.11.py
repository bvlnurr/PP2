def is_palindrome(word):
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


print(is_palindrome("madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("hello"))
