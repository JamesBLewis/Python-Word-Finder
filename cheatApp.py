# optional, colour output using the termcolor module
coloured = False

try:
    from termcolor import colored
    coloured = True
except ImportError:
    pass


# array to store possible matches (results)
results = []

# open word list (taken form OSX)
with open("words") as f:
    content = f.readlines()
# remove /n if there and get eck line of word list
content = [x.strip() for x in content]

# ask usr for word length
WordLength = raw_input("Please enter word length: ")
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
            # are all the letters in our word in the usr submitted, accepted letters
            if match == int(WordLength):
                results.append(content[lineNum])
    # incriment our loop counter
    lineNum += 1

# ask usr if they'd like the results returned and then show rsults
print("possible words: "+ str(len(results)))

# prompt usr as to if results are good enough
answer = raw_input("Do you wish to rarrow to refine search further? ")
# if they want to refine more run check for double letters
if answer == "y" or answer == "yes":
    # create array to store words we'd like to remove
    removedWords = []
    # go through each result word we have obtained and check for more letters then we are able to use
    for result in results:
        doubledLetter = []
        #convert each result word into list
        tepContentLetters = list(result)
        #for each letter in our results words see if there are repeated letters
        for letter in tepContentLetters:
            if result.count(letter) > 1:
                doubledLetter.append(letter)
        # if there is only one use of the letter in user input, add it to list of words to remove
        for dletter in doubledLetter:
            if letters.count(dletter) < 2 and result not in removedWords:
                removedWords.append(result)
    # remove invalid words found from results
    for word in removedWords:
        results.remove(word)

    # ask usr again
    answer = raw_input(str(len(results))+" words found. Do you wish to view matches? ")
    if answer == "y" or answer == "yes":
        # a nice cloured output of results unless there is no termcolor module
        for result in results:
            if coloured == True:
                print colored(result, 'green')
            else:
                print(result)
else:
    # a nice cloured output of results unless there is no termcolor module
    for result in results:
        if coloured == True:
            print colored(result, 'green')
        else:
            print(result)
