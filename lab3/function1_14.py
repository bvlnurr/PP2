def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def volume_of_sphere(radius):
    import math
    return (4/3) * math.pi * radius**3

def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

def is_palindrome(word):
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)
