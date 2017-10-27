# Patrick Kunst
# CSC 241
# Assignment 3 Part A

quote = '''A craven can be as brave as any man, when there is nothing to fear.
And we all do our duty, when there is no cost to it. How easy it seems
then, to walk the path of honor. Yet soon or late in every man's life
comes a day when it is not easy, a day when he must choose.'''

print(quote)
print('Appearances of it: ' + str(quote.count('it')))
print('Location of honor: ' + str(quote.find('honor')))

list_quote = quote.split()
print('Number of words: ' + str(len(list_quote)))

for x in list_quote:
    print(x, end = '-')

table = str.maketrans('vwsu', 'bozy')
print(quote.translate(table))
