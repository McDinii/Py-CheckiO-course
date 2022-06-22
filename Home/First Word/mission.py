def first_word(text: str) -> str:
    t = ""
    flag = False
    for i in range(len(text)):
        while ord("A") < ord(text[i]) < ord("z") or text[i] == "'":
            t += text[i]
            i += 1
            if i >= len(text):
                break
            flag = True
        if flag:
            break
    return t


if __name__ == "__main__":
    print("Example:")
    print(first_word("... don't touch it"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
