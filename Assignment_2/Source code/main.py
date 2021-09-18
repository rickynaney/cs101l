#CS 101 Lab
#Program 2
#Ricky
#rcngkd@mail.umkc.edu
print("**** Welcome to the LAB grade calculator! ****")
name=str(input("Who are we calculating grades for?"))
lab=int(input("Enter the Lab grade?=>"))
if lab < 0:
    print("The lab grade should have been zero or greater. It has been changed to 0.")
    lab=0
if lab > 100:
    print("The lab grade should have been 100 or less. It has been changed to 100.")
    lab=100
exam=int(input("Enter the exam grade?=>"))
if exam < 0:
    print("The exam grade should have been zero or greater. It has been changed to 0.")
    exam=0
if exam > 100:
    print("The exam grade should have been 100 or less. It has been changed to 100.")
    exam=100
attendance=int(input("Enter the Attendance grade?=>"))
if attendance < 0:
    print("The attendance grade should have been zero or greater. It has been changed to 0.")
    attendance=0
if attendance > 100:
    print("The attendance grade should have been 100 or less. It has been changed to 100.")
    attendance=100
grade=(lab*.7)+(exam*.2)+(attendance*.1)
print("The weighted grade for", name ,"is", grade,)
if grade < 60:
    print(name,"has a letter grade of F.")
elif grade >= 90:
    print(name,"has a letter grade of A.")
elif grade >= 80:
    print(name,"has a letter grade of B")
elif grade >= 70:
    print(name,"has a letter grade of C")
elif grade >= 60:
    print(name,"has a letter grade of D")
print("**** Thanks for using the LAB grade calculator! ****")

