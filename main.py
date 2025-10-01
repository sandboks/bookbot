from pathlib import Path
import sys

# Write a new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def OpenStringFile(filepath):
    my_file = Path(filepath)
    if not my_file.is_file():
        # print("File does not exist")
        return "ERROR: File does not exist"
    
    
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def main():
    if (len(sys.argv) < 2):
        print("USAGE:\npython3 main.py [book.txt]")
        return
    print(OpenStringFile(sys.argv[1]))
    
main()