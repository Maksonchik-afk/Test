import string

input_str = input('Введіть рядок: ')

for i in string.punctuation:
    input_str = input_str.replace(i, '')

input_str = input_str.title()
input_str = input_str.split()
hashtag = '#' + ''.join(input_str)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
