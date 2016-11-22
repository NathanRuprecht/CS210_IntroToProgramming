number_of_grades = int(input("How many grades are there: "))
sum = 0
grade = 0
As = 0
greatest = 0

for i in range(number_of_grades):
    grade = int(input("What's the grade: "))
    if grade > 90 and grade < 100:
        As += 1
    if grade > greatest:
        greatest = grade
    sum = sum + grade


avg = sum / number_of_grades

print(As, "\n",
      avg, "\n",
      greatest)
