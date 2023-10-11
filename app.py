from flask import Flask, url_for, render_template

app = Flask(__name__)


name = "BaiXi Fan"
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'}
]

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


@app.route('/index')
def index():
    return render_template('index.html', name=name, movies=movies)

if __name__ == '__main__':
    app.run()
