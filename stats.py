def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_chars(text):
    characters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def sort_chars(num_chars):
    num_chars_list = []
    for character in num_chars:
        char_dict = {
            "character": character,
            "count": num_chars[character]
        }
        num_chars_list.append(char_dict)
    num_chars_list.sort(reverse=True, key=sort_on)
    return(num_chars_list)