import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_password = os.getenv("DB_PWD")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://postgres:{db_password}@localhost:5432/example"
)

db = SQLAlchemy(app)


# --------------------------
# SQLAlchemy Model
# --------------------------
class Person(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Person ID: {self.id}, name: {self.name}>"


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    person = Person.query.first()
    return f"Hello {person.name}!"
