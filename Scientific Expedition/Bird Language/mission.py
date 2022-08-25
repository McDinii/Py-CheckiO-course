def translate(text: str) -> str:
    ans = ""
    i=0
    while i<len(text):
        ans +=text[i]
        a = text[i]

        if text[i] in "eyuioa":
            i +=3
        elif text[i] == " ":
            i+=1
        else:
            i+=2
    return ans


if __name__ == "__main__":
    print("Example:")
    print(translate("yyyooouuu duoooiiine"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
