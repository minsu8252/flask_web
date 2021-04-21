from flask import Flask , render_template, request, redirect
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


#내가 만든거---------------------------------------------------

@app.route('/data')
def data_1():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    # print(topics)
    return render_template("data.html", topics = topics)

@app.route('/data/<int:id>')
def data(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    # print(topic)
    return render_template("data_article.html", topic = topic)

@app.route('/add_data', methods=["get", "POST"])
def add_data():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author]
        
        cursor.execute(sql, input_data)
        db.commit()
        # print(cursor.rowcount)
        # db.close()
        # print(request.form['desc'])
        return redirect("/data")
    else:
        return render_template("add_data.html")


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    sql = 'DELETE FROM topic WHERE id = {};'.format(id)
    cursor.execute(sql)
    # sql = 'DELETE FROM topic WHERE id = %s;'
    # id = [id]
    # cursor.execute(sql, id)
    
    db.commit()

    return redirect("/data")

@app.route('/<int:id>/edit', methods=['POST', 'get'])
def edit(id):
    cursor = db.cursor()
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        sql = 'UPDATE topic SET title = %s, body = %s, author = %s WHERE (id = {});'.format(id)
        input_data = [title, desc, author]
        cursor.execute(sql, input_data)
        db.commit()
        return redirect('/data')
    else:
        sql = "SELECT * FROM topic WHERE id = {}".format(id)
        cursor.execute(sql)
        topic = cursor.fetchone()   
        return render_template("edit_data.html", topic = topic)


@app.route('/register',  methods=["get", "POST"])    
def register():
    cursor = db.cursor()
    if request.method == "POST":
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        sql = "INSERT INTO users (name, email, username, password) values (%s, %s, %s ,%s);"
        input_data = [name, email, username, password]

        cursor.execute(sql, input_data)
        db.commit()
        return redirect('http://localhost:5000')
    else:
        return render_template("register.html")
    



# 쌤이 만든거----------------------------------------------------

# @app.route('/articles')
# def articles():
#   sql = 'SELECT * FROM topic;'
#   cursor.execute(sql)
#   topics = cursor.fetchall()
#     # print(topics)
#   return render_template("articles.html", articles = topics)
  
# @app.route('/article/<int:id>')
# def article(id):
#     sql = 'SELECT * FROM topic WHERE id={}'.format(id)
#     cursor.execute(sql)
#     topic = cursor.fetchone()
#     print(topic)
#     # articles = Articles()
#     # article = articles[id-1]
#     # print(articles[id-1])
#     return render_template("article.html", article = article)

# @app.route('/add_articles')
# def add_articles():
#     return "<h1>글쓰기 페이지</h1>"

# 만들어 논거--------------------------------------------------------------

@app.route('/articles')
def articles():
    articles = Articles()
    # print(articles[0]['body'])
    return render_template("articles.html", articles = articles)

@app.route('/articles/<int:id>')
def article(id):
    articles = Articles()
    article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = article)

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