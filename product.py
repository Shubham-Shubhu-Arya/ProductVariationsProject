from database.db_connection import get_db_connection

class Product:
    def __init__(self, title, slug, content, image, category_id):
        self.title = title
        self.slug = slug
        self.content = content
        self.image = image
        self.category_id = category_id
        self.variations = []
        self.id = self.save_to_db()
    
    def save_to_db(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO Product (title, slug, content, image, category_id) VALUES (%s, %s, %s, %s, %s)",
            (self.title, self.slug, self.content, self.image, self.category_id)
        )
        db.commit()
        return cursor.lastrowid
