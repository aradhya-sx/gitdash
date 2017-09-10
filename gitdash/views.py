from gitdash import app
from motivate_quote_list import motivate_quote_list
from helper import generate_random_qoute, read_quotes

@app.route('/')
@app.route('/home')
def home():
    return generate_random_qoute()