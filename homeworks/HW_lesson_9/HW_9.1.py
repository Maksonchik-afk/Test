def popular_words(text, words):
    text = text.lower()
    text_words = text.split()

    result = {}

    for word in words:
        word_count = text_words.count(word)
        result[word] = word_count

    return result


print(popular_words('''When I was One I had just begun When I was Two I was nearly new''', ['i', 'was', 'three', 'near']))
