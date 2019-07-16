def reverse_word_order(input):
    list_of_words = input.split()
    return ' '.join(reversed(list_of_words))
    
reverse_word_order('Harry Potter and the prisoner of azkaban')