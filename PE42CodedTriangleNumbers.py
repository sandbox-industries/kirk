import time

def separate_words(word_to_separate):
    """take name, remove quotes and split into individual letters"""
    word_to_separate = word_to_separate.replace('"', '')
    return [char for char in word_to_separate]


def letter_to_int(butts):
    """turn letters into ints"""
    value = ord(butts)
    return value - 64

start = time.time()
with open('p042_words.txt', 'r') as words_file:
    words = words_file.read()
    wordsList = words.split(',')

triangleWords = 0

triangleNumberList = []
for n in range(1, 20):
    value = int((n * (n + 1) * 0.5))
    triangleNumberList.append(value)

for word in wordsList:
    wordScore = 0

    splitWord = separate_words(word)

    for letter in splitWord:
        letterValue = letter_to_int(letter)

        wordScore += letterValue

    if wordScore in triangleNumberList:
        triangleWords += 1

end = time.time()
totalTime = end - start
print(triangleWords, totalTime)
