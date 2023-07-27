from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UFOSighting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, nullable=False)
    details = db.Column(db.Text, nullable=False)
