def is_palindrome(text):
    text_lower = text.lower()
    filter_text = ''.join(i for i in text_lower if i.isalnum())
    return filter_text == filter_text[::-1]


r = is_palindrome('A man, a plan, a canal: Panama')
print(r)
