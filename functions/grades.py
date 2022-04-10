def print_grade(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    elif grade <= 6:
        return "Excellent"


grade_number = float(input())

print(print_grade(grade_number))