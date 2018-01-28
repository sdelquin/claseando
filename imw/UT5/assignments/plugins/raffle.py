import random

STUDENTS = [
    "Víctor Carvajal",
    "Mikeas",
    "Alfonso",
    "Omar",
    "Adrián",
    "Carlos Delgado",
    "Víctor García",
    "Yared",
    "Carlos Oliva",
    "Pablo",
    "Carmelo",
    "Adrián",
    "Sergio",
    "Noelia",
    "Kevin",
    "Roberto",
    "Alejandro",
    "Abraham",
    "Óscar"
]

PLUGINS = [str(i) for i in range(1, 102)]

GROUP_SIZE = 2
PLUGINS_PER_GROUP = 6

i = 1
while STUDENTS:
    random.shuffle(STUDENTS)
    group_members, STUDENTS = STUDENTS[:GROUP_SIZE], STUDENTS[GROUP_SIZE:]
    if len(STUDENTS) < GROUP_SIZE:
        group_members.append(STUDENTS.pop())
    random.shuffle(PLUGINS)
    assigned_plugins, PLUGINS = (PLUGINS[:PLUGINS_PER_GROUP],
                                 PLUGINS[PLUGINS_PER_GROUP:])
    print("Grupo {}: {:35} Plugins: {}".format(
        i,
        ", ".join(group_members),
        ", ".join(assigned_plugins)
    ))
    i += 1
