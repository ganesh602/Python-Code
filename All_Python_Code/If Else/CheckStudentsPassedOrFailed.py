subject1 = int(input("Enter the marks of 1st Subject : "))
subject2 = int(input("Enter the marks of 2nd Subject : "))
subject3 = int(input("Enter the marks of 3rd Subject : "))

isValidMarks = False
if (0 <= subject1 <= 100) and (0 <= subject2 <= 100) and (0 <= subject3 <= 100):
    isValidMarks = True
else:
    print(SystemExit, "Enter marks greater than 0 And Less than 100.")

if isValidMarks:
    if (subject1 >= 45) and (subject2 >= 45) and (subject3 >= 45):
        print("Congrats , You are Passed.")
    else:
        print("Sorry , You are Failed.")
