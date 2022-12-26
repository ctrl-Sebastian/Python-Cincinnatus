lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for element in iterable:
        yield count, element
        count += 1

for lessonNumber, lessonName in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(lessonNumber, lessonName))