from models.category import Category
from models.product import Product
from utils.generate_variations import generate_variations

# Taking user input
colors = input("Enter colors separated by commas: ").split(',')
sizes = input("Enter sizes separated by commas: ").split(',')
prints = input("Enter prints separated by commas: ").split(',')

attributes = {
    "color": [color.strip() for color in colors],
    "size": [size.strip() for size in sizes],
    "print": [print.strip() for print in prints]
}

# Creating category and product
category = Category("Clothing", "clothing", "Clothing category", "image.jpg")
product = Product("T-Shirt", "tshirt", "A stylish t-shirt", "tshirt.jpg", category.id)

# Generating variations
variations = generate_variations(product.id, attributes)

# Display all variations
for var in variations:
    print(var)
