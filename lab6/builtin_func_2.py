def count_case(s):
    upper = 0
    lower = 0

    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case("Hello World")