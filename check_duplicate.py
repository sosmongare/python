"""
1.	Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False. 
"""
def has_duplicate_letters(sentence):
    words = sentence.split()
    for word in words:
        letter_count = {}
        for letter in word:
            if letter in letter_count:
                return True  # Found a duplicate letter
            letter_count[letter] = 1
    return False  # No duplicate letters found


# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
result = has_duplicate_letters(sentence)
print(result)  # False

sentence = "The book is on the table"
result = has_duplicate_letters(sentence)
print(result)  # True
