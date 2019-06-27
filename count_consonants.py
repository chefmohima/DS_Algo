# count consonants in a string recursively

def count_consonant(s):
    if len(s) == 0:
        return 0
    else:
        if s[0] in 'aeiou':
            return count_consonant(s[1:])
        else:
            return 1+count_consonant(s[1:])
            
            
# test-cases
print(count_consonant('abcioujkl'))