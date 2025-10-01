# Write a new function that accepts the text from the book as a string, and returns the number of words in the string. The .split() method will be helpful here.
#Instead of printing the books contents, print this message to the console:
#Found {num_words} total words
#txt = "For only {price:.2f} dollars!"
#print(txt.format(price = 49)) 
def CountWords(s):
    return len(s.split())

#Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
#Convert any character to lowercase using the .lower() method, we don't want duplicates.
#Use a dictionary of String -> Integer. The returned dictionary should look something like this:
def CharCount(s):
    s = s.upper()
    charDict = {}
    for c in s:
        # skip, if the character is non-alphabet
        if not (c.isalpha()):
            continue
        
        if not (c in charDict):
            charDict[c] = 1
        else:
            charDict[c] += 1
    
    charDict = dict(sorted(charDict.items(), key=lambda item: item[1], reverse=True))
    return charDict
    #print (charDict)

def PrintBookReport(s):
    
    lines = [
        "============ BOOKBOT ============",
        "Analyzing book...",
        "----------- Word Count ----------",
        "Found [{n}] total words".format(n = CountWords(s)),
        "--------- Character Count -------",
        ('\n'.join([f'{key}: {value}' for key, value in CharCount(s).items()])), #"{dict}".format(dict = CharCount(s)),
        "============= END ==============="
    ]

    for line in lines:
        print(line)
    