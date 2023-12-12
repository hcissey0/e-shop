#!/usr/bin/python3
"""This is the flask app"""

from flask import Flask, render_template
from flask_login import LoginManager
from models.user import User
from models import storage
from web_flask.views import auth, main


app = Flask(__name__)
app.config['SECRET_KEY'] = b'6d2fa5eb23f9d51bb70ee66030d7e7278261020bbe84076777fe8ddd6fdd4406'

app.register_blueprint(auth)
app.register_blueprint(main)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def login_user_loader(user_id):
    return User.query(id=user_id)


@app.teardown_appcontext
def teardown(error):
    storage.close()

@app.errorhandler(404)
def errorhandlerr(error):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
