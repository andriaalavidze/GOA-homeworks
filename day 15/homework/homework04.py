def remove_spaces(word):
    word_without_space = ''
    
    for char in word:
        if char != " ":
            word_without_space = word_without_space + char
    
    print(word_without_space)

remove_spaces("Andria Alavidze")