import enchant
import string
import re
from itertools import permutations
from termcolor import cprint, colored
from scrabble_config import config


class ScrabbleHelper:

    '''
    Load in values from config file.
    '''
    def __init__(self) -> None:

        # Dictionary to check valid words against
        self.d = enchant.Dict('en_US')

        # Playable tiles
        self.letters        = config['letters']
        self.wildcard       = config['blank']
        self.extraLetters   = config['extraLetters']

        # Desired word constraints
        self.startingWith   = config['startsWith']
        self.endingWith     = config['endsWith']
        self.contains       = config['contains']
        self.pattern        = config['pattern']
        self.minLetters     = config['minWordLength']
        self.maxLetters     = config['maxWordLength']
        self.showNonMatches = config['showNonMatches']

        # Other helpers
        self.validWordFound = False
        self.printTitle = lambda x: cprint(x, 'black', 'on_blue', attrs=['bold'])
        self.printError = lambda x: cprint(x, 'black', 'on_red', attrs=['bold'])
        self.printLettersGroup = lambda x: cprint(x, 'yellow', attrs=['dark'])


    '''
    Main word finder loop.
    '''
    def solve(self):
        letters     = self.letters + self.extraLetters
        letterCount = len(letters)

        self.validWordFound = False

        try:
            for i in range(2, letterCount + 1):

                # Skip over words that dont meet minimum length requirement
                if i < self.minLetters:
                    continue

                # Skip over words that exceed max word length requirement
                if i > self.maxLetters:
                    continue

                self.printTitle(f'{i} Letters ===============')
                if self.wildcard:
                    for wildChar in string.ascii_lowercase:
                        lettersWithWildcard = letters + wildChar
                        self.findWords(lettersWithWildcard, i)
                else:
                    self.findWords(letters, i)

            if not self.validWordFound:
                self.printError('No valid words found.')

        except KeyboardInterrupt:
            self.printError('Search stopped.')


    '''
    Finds all the permutations of a group of letters, and prints the valid words.
    '''
    def findWords(self, letters, letterCount):
        permsFound = {}
        wordFoundForThisCombo = False
        combos = permutations(letters, letterCount)

        for combo in combos:
            word = ''.join(combo)

            # Skip over duplicate permutations found
            if word not in permsFound:
                permsFound[word] = True

                # Check to see if random string permutation is a valid word
                if self.d.check(word):
                    self.validWordFound = True
                    wordFoundForThisCombo = True

                    # Now that validity is confirmed, check desired word extra constraints
                    startConstraint = False
                    endConstraint = False
                    containConstraint = False
                    patternMatch = False

                    wordStr = word
                    contraintStr = ''

                    for starting in self.startingWith:
                        if starting and word.startswith(starting):
                            startConstraint = True
                            contraintStr += colored(' SRT ', 'black', 'on_cyan', attrs=['bold'])
                            break

                    for contain in self.contains:
                        if contain and contain in word:
                            containConstraint = True
                            contraintStr += colored(' CON ', 'black', 'on_green', attrs=['bold'])
                            break

                    for ending in self.endingWith:
                        if ending and word.endswith(ending):
                            endConstraint = True
                            contraintStr += colored(' END ', 'black', 'on_magenta', attrs=['bold'])
                            break

                    if self.pattern and re.match(self.pattern, word):
                        patternMatch = True
                        contraintStr += colored(' PAT ', 'black', 'on_yellow', attrs=['bold'])

                    if startConstraint or endConstraint or containConstraint or patternMatch:
                        wordStr = colored(word, 'blue', attrs=['bold'])

                    # Always show words that meet 1+ contraints
                    # Only show all other words if showNonMatches is set to True
                    if self.showNonMatches or contraintStr:
                        print(wordStr, contraintStr)

        # If any valid words were found for the group of letters passed to this function,
        # print that group of letters for reference.
        if wordFoundForThisCombo:
            self.printLettersGroup(f'--> {letters}\n')


if __name__ == '__main__':
    helper = ScrabbleHelper()
    helper.solve()
