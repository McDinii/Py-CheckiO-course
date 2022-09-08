def checkio(text: str) -> str:

    ch = ""
    text = list(text.lower())
    ma = [-1, "z"]
    for i in text:
        if i not in ch and  i in "qwertyuiopasdfghjklzxcvbnm" and(text.count(i) > ma[0] or (ma[1] > i  and ma[0] == text.count(i))):
            ma[0] = text.count(i)
            ma[1] = i
            ch += i
    return ma[1]


if __name__ == '__main__':
    print("Example:")
    print(checkio("AAaooo!!!!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
