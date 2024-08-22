def correct_sentense(text):
    text = text[0].upper() + text[1:]
    text += '.' if text[-1] != '.' else ''
    return text


result = correct_sentense("greetings, friends.")
print(result)
