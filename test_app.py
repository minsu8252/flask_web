from flask import Flask , render_template
import pymysql

test_app = Flask(__name__)

app.debug = True


@test_app.route('/test')
def test():
    # return "test 입니다."
    return render_template("test.html")

@test_app.route('/data/<int:id>')
def data(id):
    cursor = db.cursor()
    

@app.route('/data/<int:id>')
def data(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    # print(topic)
    return render_template("data_article.html", topic = topic)

if __name__ == '__main__':
    test_app.run()