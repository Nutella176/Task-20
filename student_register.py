#Ask user to input the number of students registering
students = int(input("How many students are registering? "))

#Create txt file using the write function
file = open("reg_form.txt", "w")

#Using for loop ask each student to input their student ID
#Write the student ID followed by a dotted line in the txt file
for student in range(students):
    student_id = input("Please enter you student ID: ")
    file.write(student_id)
    file.write("\n...............\n")