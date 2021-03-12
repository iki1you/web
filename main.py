from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


def main():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    user = User()

    for user in db_sess.query(User).all():
        print(user)


if __name__ == '__main__':
    main()
