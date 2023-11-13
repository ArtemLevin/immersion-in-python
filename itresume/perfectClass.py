students = []

def perfectClass(students):
    count = []
    for i in range(len(students)-1):
        if students[i] == students[i+1]:
            count.append(students[i])
    if len(students)%2 == 0:
        for student in count:
            students.remove(student)