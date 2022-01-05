grade = input("Enter grade: ")

if (grade == "A+" or grade == "a+") or (grade == "A" or grade == "a"):
    print("For this grade, you will receive a grade points of 4.0")
elif grade == "A-" or grade == "a-":
    print("For this grade, you will receive a grade points of 3.7")
elif grade == "B+" or grade == "b+":
    print("For this grade, you will receive a grade points of 3.3")
elif grade == "B" or grade == "b":
    print("For this grade, you will receive a grade points of 3.0")
elif grade == "B-" or grade == "b-":
    print("For this grade, you will receive a grade points of 2.7")
elif grade == "C+" or grade == "c+":
    print("For this grade, you will receive a grade points of 2.3")
elif grade == "C" or grade == "c":
    print("For this grade, you will receive a grade points of 2.0")
elif grade == "C-" or grade == "c-":
    print("For this grade, you will receive a grade points of 1.7")
elif grade == "D+" or grade == "d+":
    print("For this grade, you will receive a grade points of 1.3")
elif grade == "D" or grade == "d":
    print("For this grade, you will receive a grade points of 1.0")
elif grade == "F" or grade == "f":
    print("For this grade, you will receive a grade points of 0")
elif grade == "A+" or grade == "a+":
    print("For this grade, you will receive a grade points of 4.0")
else:
    print("Invalid grade entered")