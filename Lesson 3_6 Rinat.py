def int_func(*args):
    cap_word = str(word).title()
    return cap_word


text = []

for word in (input('Enter text: ').split(' ')):
    text.append(str(int_func()))

print(' '.join(text))