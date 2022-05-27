# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()


def count_words():
    text = read_file_content("./story.txt")
    result = {}
    for word in text.split():
        word = ''.join(char for char in word.lower() if char.isalnum())
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result

print(count_words())
