from youngVoice import app


@app.route('/')
def index():
    return 'hello'