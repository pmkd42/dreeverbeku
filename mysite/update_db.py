from flask_app import app, db
from models import User

if __name__ == '__main__':
    with app.app_context():
        db.create_all()