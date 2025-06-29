# +--------------------------------------------------+
# |  SCRABBLE HELPER CONFIG                          |
# |                                                  |
# |  Adjust the values below to match your scrabble  |
# |  needs. Lines that start with '#' are ignored.   |
# |  Press CTRL+C during execution to stop search.   |
# +--------------------------------------------------+

config = {

    # Playable tiles in hand
    'letters': 'dirmgl',

    # Whether or not you have a blank tile in your hand
    # Note: Currently does not support more than 1 blank
    'blank': True,

    # Additional letters from the board that you want to
    # take into consideration to form words with
    'extraLetters': '',

    # Desired word should start with any of these consecutive strings of letters
    'startsWith': [],

    # Desired word should end with any of these consecutive strings of letters
    'endsWith': [],

    # Desired word should contain any of these consecutive strings of letters
    'contains': [],

    # Desired word matches regex pattern (ADVANCED SEARCH)
    # Note: '.' matches any character, '$' matches string end
    'pattern': r'',

    # Desired word should have this many letters, minimum
    # Note: Program starts checking from length of 2 (default)
    'minWordLength': 4,

    # Desired word should have this many letters, maximum
    # Note: Program takes much longer when finding letter
    # permutations beyond 9 letters, so be patient
    'maxWordLength': 9,

    # Set this value to False if you only want to only display
    # the words that meet 1+ of the above constraints
    'showNonMatches': True,
}
