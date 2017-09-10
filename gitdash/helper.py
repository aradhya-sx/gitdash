from random import randrange
from quotes import quotes

def generate_random_qoute():
    total_quotes = len(quotes)
    random_index = randrange(0, total_quotes)
    quote = quotes[random_index]
    return quote
