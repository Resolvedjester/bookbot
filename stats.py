def get_word_count(booktext):   #splits the words/symbols and returns length
    count = booktext.split()
    return len(count)

def get_char_count(booktext):   #function to count chars, dict is initialized with a-z for readability on print
    characters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    text = booktext.lower()

    for i in text:

        if i in characters:
            characters[i] += 1

        else:
            characters[i] = 1
        
    
    return characters

def sort_char(dict):       #function makes a list of 2 key-pair dictionaries and then sorts them from greatest to lowest 
    lst =[]

    for key, value in dict.items():
        new_dict = {'character': key, 'count': value}
        lst.append(new_dict)
    
    lst.sort(key=lambda x: x['count'], reverse=True)
    
    return lst 