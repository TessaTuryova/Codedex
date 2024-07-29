# 24. Reading

books = [
    "Zero to One",
    "The Lean Startup",
    "The Mom Test",
    "Made To Stick",
    "Life In Code"
]

print(books)

books.append("Zero to Sold")  # adds string to last index of an array
books.remove("Zero to One")  # removes specified item
# books.remove("e") ValueError: list.remove(x): x not in list
books.pop(0)  # removes first item

print(books)
