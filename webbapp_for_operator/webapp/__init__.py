from flask import Flask
from webapp.db import posts
from flask_wtf.csrf import CSRFProtect
from webapp.config import SECRET_KEY, WTF_CSRF_TIME_LIMIT
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config['SECRET_KEY'] = 'ehuiwevwevwbveu'

    app.register_blueprint(user_blueprint)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
