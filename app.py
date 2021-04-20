from flask import Flask , render_template
from data import Articles
import pymysql

app = Flask(__name__)

app.debug = True

db = pymysql.connect(
    host='localhost' ,
    port = 3306 ,
    user = 'root' ,
    passwd = '1234' , 
    db = 'busan'
)

cursor = db.cursor()
#내가 만든거---------------------------------------------------

@app.route('/data')
def data_1():
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    # print(topics)
    return render_template("data.html", datas = topics)

@app.route('/data/<int:id>')
def data(id):
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    return render_template("article.html", article = topic)

@app.route('/add_data')
def add_data():
    return "<h1>글쓰기 페이지</h1>"
    

# 쌤이 만든거----------------------------------------------------

@app.route('/articles')
def articles():
  sql = 'SELECT * FROM topic;'
  cursor.execute(sql)
  topics = cursor.fetchall()
    # print(topics)
  return render_template("articles.html", articles = topics)
  
@app.route('/article/<int:id>')
def article(id):
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = article)

@app.route('/add_articles')
def add_articles():
    return "<h1>글쓰기 페이지</h1>"
# 만들어 논거--------------------------------------------------------------

# @app.route('/articles')
# def articles():
#     articles = Articles()
#     # print(articles[0]['body'])
#     return render_template("articles.html", articles = articles)

# @app.route('/article/<int:id>')
# def article(id):
#     articles = Articles()
#     article = articles[id-1]
#     print(articles[id-1])
#     return render_template("article.html", article = article)

@app.route('/', methods=['GET'])
def index():
    # return 'Hello World'
    return render_template("index.html", data = 'kim')

@app.route('/about')
def about():
    return render_template("about.html", hello = 'GARY Kim')

@app.route('/test')
def test():
    return render_template("test.html", test = '테스트')

if __name__ == '__main__':
    app.run()