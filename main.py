def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def count_words():
    content = get_book_text("books/frankenstein.txt")
    words = content.split()
    word_count = len(words)
    return print(f"{word_count} words found in the document")


def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)

count_words()