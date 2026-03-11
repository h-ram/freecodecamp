def convert_words(s):
    words = s.split(' ');
    lengths = [str(len(word)) for word in words]
    return ' '.join(lengths)