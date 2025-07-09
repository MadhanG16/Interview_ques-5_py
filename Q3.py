# Sort sentence based on embedded number in each word

def sort_sentence(sentence):
    words = sentence.split()
    words.sort(key=lambda w:[int(c) for c in w if c.isdigit()][0])
    return ' '.join([w.translate(str.maketrans('', '', '0123456789')) for w in words])

print(sort_sentence("is1 Thi0s T3est 2a"))

