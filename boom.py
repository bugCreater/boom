from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '网站建设中……'


if __name__ == '__main__':
    app.run()
