import uuid
import random
from database.db_connection import get_db_connection

class Variation:
    def __init__(self, product_id, attributes):
        self.product_id = product_id
        self.attributes = attributes
        self.sku = "SKU-" + str(uuid.uuid4())[:8]  # Generate a unique SKU
        self.price = random.randint(200, 300)  # Random price between 200-300
        self.id = self.save_to_db()
    
    def save_to_db(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO Variation (product_id, attributes, sku, price) VALUES (%s, %s, %s, %s)",
            (self.product_id, ', '.join(self.attributes), self.sku, self.price)
        )
        db.commit()
        return cursor.lastrowid
