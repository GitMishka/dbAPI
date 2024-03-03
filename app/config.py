import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

class Config:
    PG_HOST = os.environ.get("PG_HOST")
    PG_DATABASE = os.environ.get("PG_DATABASE")
    PG_USER = os.environ.get("PG_USER")
    PG_PASSWORD = os.environ.get("PG_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    db.create_all()  # Creates the database tables based on  models (if they don't exist)
    app.run(debug=True)
