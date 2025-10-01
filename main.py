# Write a new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def OpenStringFile(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        contents = f.read()
        return contents
    
def main():
    print(OpenStringFile("books/frankenstein.txt"))
    
main()