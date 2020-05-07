import time

# open file, split and alphabetize names
with open("p022_names.txt", "r") as namesFile:
    names = namesFile.read()
    nameList = sorted(names.split(","))


# take name, remove quotes and split into individual letters
def separate_names(name_to_separate):
    name_to_separate = name_to_separate.replace('"', '')
    return [char for char in name_to_separate]


# turn letters into ints
def letter_to_int(letter):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return alphabet.index(letter) + 1


start = time.time()
total = 0
# grab name from list
for name in nameList:
    nameScore = 0
    namePlace = nameList.index(name) + 1

    # take name, remove quotes, split into individual letters
    splitName = separate_names(name)

    # take each letter and convert it to an int
    for letter in splitName:
        letterValue = letter_to_int(letter)

        # add up name score
        nameScore += letterValue

    total = total + (nameScore * namePlace)

end = time.time()
timeElapsed = end - start
print(total, timeElapsed)
