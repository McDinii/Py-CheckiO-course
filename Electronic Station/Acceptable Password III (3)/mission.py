def is_acceptable_password(password: str) -> bool:
    flag_D,flag_L = False,False
    for i in password:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            flag_D = True
        elif i in "qwertyuiopasdfghjklzxcvbnm":
            flag_L = True
        if flag_L and flag_D and len(password) > 6 :
            return True
    return False



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
