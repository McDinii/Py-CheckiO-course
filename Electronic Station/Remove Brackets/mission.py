def remove_brackets(line: str) -> str:
    ch = [line[0]]
    ans = line[0]
    for i in line[1:]:
        ans += i
        if ch[-1] + i in ["()", "{}", "[]"]:
            ans += i
            ch = ch[:-1]  # удалили из стека последнюю скобку
            continue
        elif i in ["]",")","}"]:
            ans = ans[:-2]
            ch = ch[:-2]
        ch.append(i)
    return ans[:-1]


if __name__ == "__main__":
    print("Example:")
    print(remove_brackets("[[(}]]"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets("(()()") == "()()"
    assert remove_brackets("[][[[") == "[]"
    assert remove_brackets("[[(}]]") == "[[]]"
    assert remove_brackets("[[{}()]]") == "[[{}()]]"
    assert remove_brackets("[[[[[[") == ""
    assert remove_brackets("[[[[}") == ""
    assert remove_brackets("") == ""
    assert remove_brackets("[(])") == "()"
    print("Coding complete? Click 'Check' to earn cool rewards!")
