from gitdash import app
from motivate_quote_list import motivate_quote_list
from helper import generate_random_qoute, read_quotes

@app.route('/')
@app.route('/home')
def home():
    quotes = read_quotes('quotes.txt')
    authors = list(set(author for _, author in quotes))
    quote, _ = random.choice(quotes)
    author = random.choice(authors)
    print quote.encode('utf-8'), '-', author.encode('utf-8')
    return generate_random_qoute()