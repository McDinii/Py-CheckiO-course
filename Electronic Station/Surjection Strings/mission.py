def replace(str):
    c = 1
    new_a = ""
    i = 0
    while i < len(str):
        if i + 1 < len(str):
            ch = c
            if str[i] == str[i + 1]:
                let = str[i]
                i += 1
                while i < len(str) and str[i] == let:
                    c += 1
                    i += 1
                new_a += "&" * c
            else:
                new_a += "*"

        else:
            new_a += "*"
        i += 1
    return new_a
def isometric_strings(a, b):
    # print(a,b)
    # print(replace(a),replace(b))
    # if replace(a) == replace(b):
    #     return True
    # return False
    cipher = {}
    for i, c in enumerate(a):
        if c not in cipher:
            cipher[c] = b[i]
        elif cipher[c] != b[i]:
            return False
    print(cipher)

    return True
if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("bar", "foo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("adg", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
