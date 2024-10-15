score = int(input("Marks: "))
if score > 90:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
else:
    grade = 'D'

print(f"Your grade is: {grade}")