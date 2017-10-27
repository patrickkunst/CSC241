# Patrick Kunst
# CSC 241
# Assignment 4

name = input('Enter Text File Name: ')
inFile = open(name)
criteria = input('Enter Text to Search For: ')

name_split = name.split('.txt')
file_name = name_split[0] + '_out.txt'
outFile = open(file_name, 'w')


def searchFile(file, search):

    '''This function takes two parameters, a file and a search criteria string.
       It counts the appearances in the file, and also writes all the appearances
       Along with the line number in a new file.'''

    inLines = []
    lineIndex = []
    text = file.readlines()
    search_count = 0

    for x in text:
        if search in x:
            search_count += x.count(search) # To count all appearances in line
            if x not in inLines:# So the line is not double-added
                # If true, the line and index are added to two separate lists
                inLines.append(x)
                lineIndex.append(text.index(x))

    y = 0

    for x in lineIndex:
        # Formats the output into the file using the lists
        linefmt = '{}) {}'
        outFile.write(linefmt.format(lineIndex[y], inLines[y]))
        y += 1

    outFile.flush() #I did not write this and I spend 30 minutes trying to wonder why the file wasn't being written to
    outFile.close()
    return search_count


count = searchFile(inFile, criteria)

print(criteria + ' appears in ' + name + ' ' + str(count) + ' times')
