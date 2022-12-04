from os import system

# index	students_first_name	students_last_name	students_age
#   0	    Juli	            Pierre	            21
#   1	    John	            Kosh	            20
#   ...	    ...         	    ...	                ...
#   n	    ...                 ...	                ...

#system("clear")

students_first_name = []
students_last_name  = []
students_age        = []
student_mark        = []



students_first_name.append("Juli")
students_last_name.append("Pierre")
students_age.append(21)
student_mark.append(9.5)

while True:
    new_student = input("Enter students data: ")
    if new_student == "":
        break
    else: pass
# split the string on single str elements    
    x = new_student.split()

# added new data in our lists
    students_first_name.append(x[0])
    students_last_name.append(x[1])
    if 18 <= int(x[2]) <= 30:
        students_age.append(x[2])
    else:
        print("Your age does not fit")
        break
    if 0.01 <= float(x[3]) <= 10.00:
        student_mark.append(x[3])
    else:
        print("You mark does not fit")
        break

# printing out list with new data
    for i in range(len(students_first_name)):
        print(students_first_name[i], 
               students_last_name[i], 
                     students_age[i], 
                     student_mark[i])
        






# printing out list with new data
#    print(students_first_name)
#    print(students_last_name)
#    print(students_age)
