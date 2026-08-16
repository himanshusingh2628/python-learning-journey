# Python Dictionaries

student = {
    "name": "Himanshu",
    "course": "B.Tech CSE",
    "skill": "Python",
    "year": 1
}

print("Student Details:")

for key, value in student.items():
    print(key, ":", value)

print("\nStudent Name:", student["name"])
print("Course:", student["course"])
