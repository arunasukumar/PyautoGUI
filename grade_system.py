try:
    marks = int(input("Enter the marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a number between 0 and 100.")
    elif marks >=90:
        print("marks:", marks,"\nGrade A")
    elif marks >=80:
        print("marks:", marks,"\nGrade B")
    elif marks >=70:
        print("marks:", marks,"\nGrade C")
    elif marks >=60:
        print("marks:", marks, "\nGrade D")
    else:
        print("marks:", marks,"\nGrade E")  
except ValueError:
        print("Invalid input! Please enter numbers only.")     
