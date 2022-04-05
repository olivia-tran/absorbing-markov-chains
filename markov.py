"""Generate Markov text from text files."""
from importlib.resources import contents
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as f:
        contents = f.read()  # read entire contents

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    all_words = text_string.split()
    all_words.append(None)
    """bigrams (key), pick a next word, add all these 3 words to our result, bigrams[1]+next_word = current_bigrams, again pick the next word"""
    for i in range(len(all_words)-2):
        bigrams = (all_words[i], all_words[i+1])
        next_word = all_words[i+2]
        if bigrams not in chains:
            chains[bigrams] = []

        chains[bigrams].append(next_word)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # use choice to pick a random key from chains.keys()
    current_bigram = choice(list(chains.keys()))
    # add the starting bigram to result list
    words += current_bigram
    # pick next word that followed current bigram in chains
    next_word = choice(chains[current_bigram])
    # add while loop
    while next_word is not None:  # until we exhaust the list of next word
        # new tuple keys for the chains dict (previous_bigram[1] + next_word)
        current_bigram = (current_bigram[1], next_word)
        # add next_word to words
        words.append(next_word)
        #dict.get('key', default_value)

        next_word = choice(chains[current_bigram])

    return ' '.join(words) + '\n\n'


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
