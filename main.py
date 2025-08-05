def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)

main()