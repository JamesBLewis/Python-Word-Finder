# array to store possible matches (results)
results = []

# ask usr for word length
WordLength = raw_input("Please enter word length: ")
# open OSX dictionary
with open("/usr/share/dict/words") as f:
    content = f.readlines()
# remove /n if there and get eck line of word list
content = [x.strip() for x in content]

# print to check if we were able to actually get any words from the computer
print(str(len(content))+" words loaded")

#prompt for letters they want to check
letters = raw_input("Please enter possible letters: ")
print("searching...")

# remove spaces if usr is stupid
letters = letters.replace(" ","")

# line number counter
lineNum = 0
# loop through lines
while lineNum < len(content):
    # carate var to store the number of letter matches
    match = 0
    # filter out words of the wrong length
    if len(content[lineNum]) == int(WordLength):
            # store the word on this line in an array of letters
            tepContentLetters = list(content[lineNum])
            # is every letter in our list of accepted letters?
            # if so increment our match counter.
            for letter in tepContentLetters:
                if letter in letters:
                    match += 1
            #are all the letters in our word in the usr submitted, accepted letters
            if match == int(WordLength):
                results.append(content[lineNum])
    #incriment our loop counter
    lineNum += 1

# ask usr if they'd like the results returned and then show rsults
print("possible words: "+ str(len(results)))
answer = raw_input("Do you wish to see them all? ")
if answer == "y" or answer == "yes":
    print(results)
