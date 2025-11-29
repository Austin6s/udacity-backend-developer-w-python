import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_password = os.getenv("DB_PWD")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://postgres:{db_password}@localhost:5432/example"
)

db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hello World!"
