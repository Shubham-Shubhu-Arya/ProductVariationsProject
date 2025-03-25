from datetime import datetime
from database.db_connection import get_db_connection

class Category:
    def __init__(self, title, slug, content, image):
        self.title = title
        self.slug = slug
        self.content = content
        self.image = image
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = self.save_to_db()
    
    def save_to_db(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO Category (title, slug, content, image, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.title, self.slug, self.content, self.image, self.created_at, self.updated_at)
        )
        db.commit()
        return cursor.lastrowid
