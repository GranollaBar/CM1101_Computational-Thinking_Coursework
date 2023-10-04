skip_words = ['', 'a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', 'magic', 'entrance', 'cell', 'pink', 'blade', 
              'rubble', 'prison']

def remove_punct(text):
    '''removes punctuation from the users input'''
    return_string = ""
    for char in text:
        if char.isalpha() or char.isnumeric() or char == " ":
            return_string += char
    return return_string

def filter_words(words):
    '''removes words that are in the skip_words list as they are classed as irrelevent words'''
    filtered_words = []
    for word in words:
        if not word in skip_words:
            filtered_words.append(word)
    return filtered_words

def normalise_text(player_input):
    '''changer the user input all to lower case, and removes all irrelevent words and punctuation by calling the 
    remove_punct() and filter_words()functions '''
    return filter_words(remove_punct(player_input).lower().split(" "))
