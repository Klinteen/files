
def find_anagram():
    pass
    # Check if two words are anagrams
    # Example:
    # find_anagrams("hello", "check") --> False
    # find_anagrams("below", "elbow") --> True

    Word = "Fill in the words of your choice"
    print(Word)

    word1 = input ("First Word: ")
    word2 = input ("Second Word: ")
    if (sorted(word1) == sorted(word2)):
        return True
        print("The strings are anagrams")
    else:
        return False
        print("The strings aren't anagrams")


print(find_anagram())

