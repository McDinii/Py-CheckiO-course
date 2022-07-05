def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    wordD = text.split()
    dict_ = dict()
    for i in wordD:
        val = wordD.count(i)
        if str(i) in words:
            dict_[str(i)] = val
    for i in words:
        if i not in dict_.keys():
            dict_[i] = 0
    return dict_


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))


    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    print("Coding complete? Click 'Check' to earn cool rewards!")
