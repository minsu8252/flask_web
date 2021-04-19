from flask import Flask , render_template
from data import Articles

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
    # return 'Hello World'
    return render_template("index.html", data = 'kim')

@app.route('/about')
def about():
    return render_template("about.html", hello = 'GARY Kim')

@app.route('/articles')
def articles():
    articles = Articles()
    # print(articles[0]['body'])
    return render_template("articles.html", articles = articles)

@app.route('/test')
def test():
    return render_template("test.html", test = '테스트')

if __name__ == '__main__':
    app.run()