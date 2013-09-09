from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello stranger!'

@app.route('/')
def index():
    return 'Front Page!'


if __name__ == '__main__':
    app.run()
