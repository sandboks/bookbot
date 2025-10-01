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
    return 0

