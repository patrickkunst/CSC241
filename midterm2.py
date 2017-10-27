# Patrick Kunst
# CSC 241
# Midterm 2

def complexity(words):
    sum_chars = 0
    counted_words = []
    for x in words:
        if len(x) >= 4:
            counted_words.append(x)
    for y in counted_words:        
        sum_chars += len(y)

    lex = sum_chars / len(counted_words)
    return lex


file_name = input('Enter the text file name: ')
file = open(file_name)
text = file.read()
text = text.replace('\n', ' ') #Otherwise when splitting, new lines don't make a new word
word_list = text.split(' ')



lexical_complexity = complexity(word_list)
print('File ' + file_name + ' has a lexical complexity of ' + str(lexical_complexity))
