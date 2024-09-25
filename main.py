def read_text_file (filepath):
    with open(filepath) as f:
        file_contents = f.read() 
    return file_contents 

def count_words (text_string):
    words = text_string.split()
    return len(words)

def count_characters (text_string):
    character_appearances = {}
    character_list = []
    lowered_text_string = text_string.lower()

    for text in lowered_text_string:
        if text in character_appearances:
            character_appearances[text] += 1 
        else:
            character_appearances[text] = 1

    for key in character_appearances:
        if key.isalpha():
            character_list.append({"count": character_appearances[key], "key": key})

    return character_list 

def sort_on(dict):
    return dict["count"]
    

def main () :
    book_filepath = "books/frankenstein.txt"
    text = read_text_file(book_filepath)
    print(f"--- Begin report of {book_filepath} ---")
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    print()
    char_list = count_characters(text)
    char_list.sort(reverse=True, key=sort_on)
    for word_obj in char_list:
        print(f"The '{word_obj['key']}' character was found {word_obj['count']} times")
    print("--- End report ---")

main ()
