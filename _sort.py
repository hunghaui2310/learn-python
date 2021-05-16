# sort() method = used with lists
# sort() function = used with iterables

students = ["Paul", "Peter", "Laura", "John"]
teachers = ("Paul", "Peter", "Laura", "John")
persons = [
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Mr.Krabs", "C", 78),
    ("Squidward", "F", 60),
]

students.sort(reverse=True)
sorted_teacher = sorted(teachers, reverse=True)

grade = lambda grades: grades[2]
persons.sort(key=grade, reverse=True)

for i in students:
    print(i)

for i in teachers:
    print(i)

for i in persons:
    print(i)