import string
# import re
import PyPDF2
import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def tokenize(text) -> list:
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3, strip digits.
    """
    text = text.lower()
    text = re.sub('[' + string.punctuation + '0-9\\r\\t\\n]', ' ', text)
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if len(w) > 2]
    tokenized_words = [t for t in tokens if t not in ENGLISH_STOP_WORDS]
    return tokenized_words


def stemwords(words) -> list:
    """
    Given a list of tokens/words, returns a new list with each word
    stemmed using a PorterStemmer.

    NOTICE that this function probably isn't needed. (see notebook)
    """
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(w) for w in words]
    return stemmed_words


def list_corpus(reader_obj) -> list:
    """
    Given a reader_obj, returns a list of strings. Each string is a page
    of text extracted from the PDF. If we wanted a 2D list of each word just remove .join
    """
    pages = []
    for i in range(len(reader_obj.pages)):
        reader_text = bluebook.pages[i].extract_text()
        token = tokenize(reader_text)
        pages.append(" ".join(token))
    return pages
