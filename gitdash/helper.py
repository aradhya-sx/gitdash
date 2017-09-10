from motivate_quote_list import motivate_quote_list
from random import randrange


def read_quotes(filename):
    with open('quotes.json') as f:
        lines = (l.strip() for l in f)
        return [json.loads(l.decode('utf-8')) for l in lines if l]
        
def generate_random_qoute():
	total_quotes = len(motivate_quote_list)
	random_index = randrange(0, total_quotes)
	return motivate_quote_list[random_index]
