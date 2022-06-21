from queue import Empty


positionlist = []
word = input("Input a word plzplz")
len(word)
character = input("Which index of a letter would you like to know from the word you last inputted: ")
for position, letter in enumerate(word):
    if letter == character:
        positionlist.append(position)

if len(positionlist) > 0:
    print(positionlist)
else:
    print("There were no such letters")