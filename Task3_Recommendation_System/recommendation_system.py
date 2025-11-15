products = {
    "electronics": ["Smartphone", "Laptop", "Headphones", "Smartwatch"],
    "fashion": ["Jeans", "T-Shirt", "Shoes", "Jacket", "Accessories"],
    "books": ["Fiction", "Non-Fiction", "Mystery", "Self-Help", "Spiritual", "Comics"],
    "beauty": ["Face Cream", "Perfume", "Makeup Kit", "Body Lotion"],
    "groceries": ["Rice", "Milk", "Eggs", "Bread", "Sugar", "Flour","Maggiee"],
    "fruits and vegetables": ["Apple", "Banana", "Tomato", "Potato", "Cucumber"]
}
print("=== Simple Recommendation System ===")
print("Available categories:\n")

for category in products:
    print("-", category.capitalize())
choice = input("\nEnter a category you like: ").lower()
if choice in products:
    print("\nBased on your interest, you may like:\n")
    for item in products[choice]:
        print("- " + item)
else:
    print("\nSorry, that category is not available.")
