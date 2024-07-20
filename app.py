# from flask import Flask
# from models import db, Employee
# from routes import main as main_blueprint
# from config import Config

# app = Flask(__name__)
# app.config.from_object(Config)

# db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# app.register_blueprint(main_blueprint)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from models import db, Employee
from routes import main as main_blueprint
from config import Config
import flask

# Check Flask version
print("Flask version:", flask._version_)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.register_blueprint(main_blueprint)

if __name__ == "_main_":
    app.run(debug=True)
