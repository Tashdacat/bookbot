def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def count_words():
    content = get_book_text("books/frankenstein.txt")
    words = content.split()
    word_count = len(words)
    return f"Found {word_count} total words found in the document"

def count_characters():
    content = get_book_text("books/frankenstein.txt")
    lowered = content.lower()
    characters = list(lowered)
    char_count = {}
    for char in characters:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort():
    char_count = count_characters()
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return "\n".join(f"{char}: {count}" for char, count in sorted_chars)
    
def book_report():  
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{count_words()}
--------- Character Count -------
{sort()}
============= END ===============
        """)