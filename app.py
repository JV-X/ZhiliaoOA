from flask import Flask
from exts import db
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp

import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
