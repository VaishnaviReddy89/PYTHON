print("+-------STUDENT MARKS PROCESSING-------+")
MARKS=input("ENTER STUDENTS MARKS: ")

print("ENTER CONVERSION TYPE")
print("1.IF YOU WANT TO CONVERT TO INTEGER THEN CHOOSE THESE OPTION")
print("2.IF YOU WANT TO CONVERT TO FLOAT THEN CHOOSE THESE OPTION")

choice=int(input("enter a choice: "))
if choice==1:
    print("INTEGER VALUE: ", int(float(MARKS)))
elif choice==2:
    print("FLOAT VALUE: ",float(MARKS))
else:
    print("YOU ARE CHOOSEN INVALID CHOICE SO PLEASE TRY AGAIN!!!!")
#✔️

#🧠 Rule to remember

#Whenever input may contain decimals:

#Always convert string → float → int

#Never do:

#string → int → float