def words_order(text: str, words: list) -> bool:
    text = text.split()
    ind = -1
    ch = 0
    if len(set(words)) != len(words):
        return False
    for i in range(len(words)):
        for j in range(len(text)):
            if words[i] == text[j] and words[i] in text:
                if j < ind:
                    return False
                ind = j
                ch +=1
                break
        if ch == len(words):
            return True
    return False
if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here hi world im here", ["word", "world"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
