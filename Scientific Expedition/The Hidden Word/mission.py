def checkio(text, word):
    i = 0
    buf = []
    n_txt = []
    text = text.lower()
    x, y, xe, ye = 0, 0, 0, 0

    while i < len(text):
        if text[i] == " ":
            i += 1
            continue
        elif text[i] == "\n":
            n_txt.append(buf)
            buf = []
            i += 1
        else:
            buf.append(text[i])
            i += 1
    n_word = ""
    word1 = word
    chn = 1
    for i in range(len(n_txt)):
        for j in range(len(n_txt[i])):
            ch = n_txt[i][j]
            if n_txt[i][j] == word1[0] and n_word == "" and (n_txt[i + 1][j] == word1[1] or n_txt[i][j + 1] == word1[1]):
                n_word += word[0]
                word = word[1:]
                x = i + 1
                y = j + 1
            elif n_word + n_txt[i][j] == word1 and n_word != '' and (
                    n_txt[i + 1][j] == word1[chn] or n_txt[i][ j + 1] == word1[chn]):
                xe = i + 1
                word = word[1:]
                ye = j + 1
                chn += 1
            elif n_txt[i][j] == word[0] and n_word != "" and (i + 1 == x or j + 1 == y) and (
                    n_txt[i + 1][j] == word1[chn] or n_txt[i][j + 1] == word1[chn]):
                n_word += word[0]
                word = word[1:]
                chn += 1

    return [x, y, xe, ye]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("""Hetookhisvorpalswordinhand:
                     Longtimethemanxomefoehesought--
                     So rested he by the Tumtum tree,
                     Andstoodawhileinthought.
                     Andasinuffishthoughthestood,
                     TheJabberwock,with eyes of flame,
                     Camewhifflingthrough the tulgey wood,
                     And burbled as it came!""", "noir"))
    assert checkio("""DREAMING of apples on a wall,
                      And dreaming often, dear,
                      I dreamed that, if I counted all,
                      -How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
