from gitdash import app
from helper import generate_random_qoute

@app.route('/')
@app.route('/home')
def home():
    return generate_random_qoute()