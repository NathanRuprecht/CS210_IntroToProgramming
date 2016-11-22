number_of_grades = int(input("How many grades are there: "))
sum = 0
grade = 0

for i in range(number_of_grades):
    grade = int(input("What's the grade: "))
    sum = sum + grade


avg = sum / number_of_grades

print(avg)
