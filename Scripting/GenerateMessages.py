names =  input("Names: ")
assignments =  input("Assignments: ")
grades =  input("Grades: ")

namesList = names.split(",")
assignmentsList = assignments.split(",")
gradesList = grades.split(",")

"""
print(namesList)
print(assignmentsList)
print(gradesList)
"""
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

"""
for nombre, tareas, nota in namesList, assignmentsList, gradesList:
    potentialGrade = nota + (2 * tareas)
    print(message.format(nombre, tareas, nota, potentialGrade))
    
"""

for n, a, g in zip(namesList, assignmentsList, gradesList):
    print(message.format(n, a, g, int(g) + int(a)*2))