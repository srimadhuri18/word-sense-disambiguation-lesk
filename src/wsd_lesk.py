import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


def word_sense_disambiguation(sentence, ambiguous_word):

    tokens = word_tokenize(sentence)

    sense = lesk(tokens, ambiguous_word)

    return sense