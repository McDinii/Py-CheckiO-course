def between_markers(text: str, begin: str, end: str) -> str:
    ans = ""
    for i in range(len(text)):
        if text[i] == begin:
            i +=1
            while text[i] != end:
                ans += text[i]
                i+=1
            break
    return ans


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
