num_course = int(input("lessons count"))
sum = 0
sum_unit = 0
count_unit = 0
courses = []
for i in range (num_course):

    name = str(input("enter course name"))
    grade = float(input("enter your grade"))
    unit = int(input("enter your unit"))

    
    sum_unit = grade * unit
    sum = sum + sum_unit
    count_unit = count_unit + unit
    courses.append([name,grade,unit])

print("================================")

print(courses)

for course in courses:
    print(f"course name{course[0]}")
    print(f"course grade{course[1]}")
    print(f"course unit{course[2]}")
print("================================")
avg = sum / count_unit
print("your overall",avg)