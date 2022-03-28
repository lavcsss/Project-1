student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    if student_scores[names] > 90 and student_scores[names] < 100:
        grade = "Outstanding"
    elif student_scores[names] > 80 and student_scores[names] < 90:
        grade = "Exceeds Expectations"
    elif student_scores[names] > 70 and student_scores[names] < 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[names] = grade 
    

# 🚨 Don't change the code below 👇
print(student_grades)