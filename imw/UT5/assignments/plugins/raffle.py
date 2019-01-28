import random

PLUGINS_PER_STUDENT = 3

with open('students.txt') as f:
    students = [student.strip() for student in f.readlines()]
plugins = list(range(1, (len(students) * PLUGINS_PER_STUDENT) + 1))

while students:
    # pick a random student
    random.shuffle(students)
    picked_student = students.pop()

    # pick random plugins
    random.shuffle(plugins)
    picked_plugins = [plugins.pop() for _ in range(PLUGINS_PER_STUDENT)]

    print(picked_student, picked_plugins)
