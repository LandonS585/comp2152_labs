#Q1
grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort
print(f"Sorted Grades: {grades}")
print(f"Highest Grade: {grades[-1]}")
print(f"lowest Grade: {grades[0]}")
print(f"Total Number of Grades: {len(grades)}")

#Q2
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
print(f"position of milk: {cart.index("milk")}")
cart.remove("apple")
print(f"Removed item using pop: {cart.pop()}")
print("Is banana in the cart?", "banana" in cart)
print(f"Final cart: {cart}")

#Q3
point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1)  2 + (y2 - y1)  2) ** 0.5

characters = tuple("PYTHON")

print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)
print("Characters tuple:", characters)

for char in characters:
    print(char)

#Q4
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both_classes = monday_class & wednesday_class
either_class = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one_class = monday_class ^ wednesday_class

is_subset = monday_class <= either_class

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both_classes)
print("Attended either class:", either_class)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one_class)
print("Is Monday subset of all students?", is_subset)

#Q5
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())

print("Total contacts:", len(contacts))