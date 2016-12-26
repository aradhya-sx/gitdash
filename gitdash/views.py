from gitdash import app

@app.route('/')
@app.route('/home')
def home():
    return "Hey"