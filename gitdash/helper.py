from random import randrange
from quotes import quotes
import unicodedata


def generate_random_qoute():
    total_quotes = len(quotes)
    random_index = randrange(0, total_quotes)
    quote = quotes[random_index]
    q = unicodedata.normalize('NFKD', quote).encode('ascii','ignore')
    return q
