from datetime import datetime
import re

from app import db


def slugify(string):
    pattern = r'[^\w+]'
    return re.sub(pattern, '_', string)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    content = db.Column(db.Text)
    created = db.Column(db.Datetime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'
