from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello():  # put application's code here
    # return '欢迎来到我的WatchList!'
    return '<h1> Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/home')
def home():
    return "Welcome to My Watchlist"


@app.route('/user/<name>')
def user_page(name):
    return "<h1>User: {}</h1>".format(name)


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='XiFan'))
    print(url_for('user_page', name='Peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'


if __name__ == '__main__':
    app.run()
