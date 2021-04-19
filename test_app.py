from flask import Flask , render_template

test_app = Flask(__name__)

@test_app.route('/test')
def test():
    # return "test 입니다."
    return render_template("test.html")

if __name__ == '__main__':
    test_app.run()