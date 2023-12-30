def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_letters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print_report(num_words,char_dict)
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        letters[letter] = letters.get(letter, 0) + 1
    
    return letters

def print_report(num_words, char_dict):
    print(f"{num_words} words found in the document\n")
    for c in char_dict:
        if c.isalpha():
            print(f"The '{c}' character was found {char_dict[c]} times")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()