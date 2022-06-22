def backward_string_by_word(text: str) -> str:
    arr = text.split()
    str_ = ""
    j = 0
    for i in arr:
        str_ += i[::-1]
        j += len(i)
        while j < len(text) and text[j]== " ":
            str_ += " "
            j += 1
    return str_


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('welcome to a game'))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
