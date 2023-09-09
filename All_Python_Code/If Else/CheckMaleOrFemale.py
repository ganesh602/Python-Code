print("Write Your Gender : Male or Female : ")
gender = input("Male or Female : ")

if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
    print("You are a Male.")
elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
    print("You are a Female.")
else:
    print("Write properly.")

