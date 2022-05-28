# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

    if len(word) != len(anagram):
        return False

    word_dict = {}
    anagram_dict = {}

    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    for letter in anagram:
        if letter in anagram_dict:
            anagram_dict[letter] += 1
        else:
            anagram_dict[letter] = 1

    if word_dict == anagram_dict:
        return True
    else:
        return False


print(find_anagram("below", "elbow"))
