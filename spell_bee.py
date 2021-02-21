import pdb
WORDLIST_FILENAME = "/home/travis/word_list/words_alpha.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def playGame(wordList, center_letter, remaining_letters):
    """
    Plays a game of Spell Bee, see NY Times mini game
    """
    little_list = []
    inWord = True
    # pdb.set_trace()
    for word in wordList:
        if (len(word) > 3) and (center_letter in word):

            # ######
            for letter in word:
                if (letter not in remaining_letters) and \
                        (letter != center_letter):
                    inWord = False
                    break
            if inWord:
                little_list.append(word)
        inWord = True

    outFile = open("outWordList.txt", 'w')
    for myWord in little_list:
        outFile.write("%s\n" % myWord)
    outFile.close()


if __name__ == '__main__':
    wordList = loadWords()
    # load letters in lowercase
    center_letter = "m"
    remaining_letters = "rfaldn"
    playGame(wordList, center_letter, remaining_letters)
