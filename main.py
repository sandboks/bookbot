from pathlib import Path
import sys

from stats import CountWords
from stats import CharCount
from stats import PrintBookReport

def FileExists(filepath):
    my_file = Path(filepath)
    return my_file.is_file()

# Write a new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def OpenStringFile(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents



def main():
    if (len(sys.argv) < 2):
        print("USAGE:\npython3 main.py [book.txt]")
        return
    
    filepath = sys.argv[1]

    if not FileExists(filepath):
        print("ERROR: File does not exist")
        return
    
    s = OpenStringFile(filepath)
    countMsg = "Found [{n}] total words"
    #print(countMsg.format(n = CountWords(s)))

    #CharCount(s)
    PrintBookReport(s)
    #print(CharCount(s))
    
    #print(s)
    
main()