# 1. Input Validation Functions
def get_valid_students_number():
    while True:
        num = int(input("How many students do you want to evaluate? "))
        if num > 0:
            return num
        print("Invalid number. Please enter a number greater than 0.")
def get_valid_score(prompt):
    while True:
        score = int(input(prompt))
        if 0 <= score <= 100:
            return score
        print("Invalid score. Please enter a number between 0 and 100.")
def calculate_final_grade(attendance, homework, quiz, participation):
    return (attendance * 0.20) + (homework * 0.35) + (quiz * 0.35) + (participation * 0.10)
def get_student_status(final_grade, attendance):
    if attendance < 50:
        return "Failed because of low attendance"
    elif final_grade >= 85:
        return "Excellent"
    elif final_grade >= 70:
        return "Good"
    elif final_grade >= 50:
        return "Needs Improvement"
    else:
        return "Failed"
def get_student_advice(attendance, homework, quiz, participation):
    if attendance < 50:
        return "You need to attend more sessions."
    if homework < 50:
        return "You need to focus more on homework."
    if quiz < 50:
        return "You need to study more for quizzes."
    if participation < 50:
        return "Try to participate more during sessions."
    return "Keep up the good work."
def print_student_report(name, final_grade, status, advice):
    print("\nStudent Report")
    print(f"Name: {name}")
    print(f"Final Grade: {final_grade: }")
    print(f"Status: {status}")
    print(f"Advice: {advice}")
# Main program
# Step 1: Get number of students (with validation)
def main():
    total_students = get_valid_students_number()
    excellent_count = 0
    good_count = 0
    need_improvement_count = 0
    failed_count = 0
    total_grades = 0
    highest_grade = -1
    lowest_grade = 101
 # Step 2: Repeat for each student
    for i in range(1, total_students + 1):
        print(f"\nStudent {i}")
        name = input("Enter student name: ")
        
        attendance = get_valid_score("Enter attendance score: ")
        homework = get_valid_score("Enter homework score: ")
        quiz = get_valid_score("Enter quiz score: ")
        participation = get_valid_score("Enter participation score: ")
        
        # Step 3: Calculate final grade
        final_grade = calculate_final_grade(attendance, homework, quiz, participation)
        
        # Step 4: Decide student status
        status = get_student_status(final_grade, attendance)
        
        # Challenge: Get advice
        advice = get_student_advice(attendance, homework, quiz, participation)
        
        # Print student report
        print_student_report(name, final_grade, status, advice)
        
        # Update statistics
        total_grades += final_grade
        if final_grade > highest_grade:
            highest_grade = final_grade
        if final_grade < lowest_grade:
            lowest_grade = final_grade
        
        if status == "Excellent":
            excellent_count += 1
        elif status == "Good":
            good_count += 1
        elif status == "Needs Improvement":
            need_improvement_count += 1
        else:  # "Failed because of low attendance" or "Failed"
            failed_count += 1
    
    # Final Group Summary
    class_average = total_grades / total_students
    print("\nFinal Group Summary")
    print(f"Total students: {total_students}")
    print(f"Excellent students: {excellent_count}")
    print(f"Good students: {good_count}")
    print(f"Needs improvement: {need_improvement_count}")
    print(f"Failed students: {failed_count}")
    print(f"Class average: {class_average:.2f}")
    print(f"Highest grade: {highest_grade:.1f}")
    print(f"Lowest grade: {lowest_grade:.1f}")
    
main()
