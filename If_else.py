def getGrade(perc):
 if perc < 35:
  grade = "FAIL"
 elif perc >= 35 and perc <= 50:
  grade = "Third Division"
 elif perc > 50 and perc < 65:
  grade = "Second Division"
 else:
  grade = "First Division"
 return grade
perc = input("Enter the percentage")
print(" The grade is : ",getGrade(int(perc)))