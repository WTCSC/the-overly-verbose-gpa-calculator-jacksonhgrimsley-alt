def get_valid_grade(index):
    while True:
        try:
            grade = float(input(f"Enter grade {index+1} (0.0-4.0): "))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("❌ That grade is out of range. Try again.")
        except ValueError:
            print("❌ Not a valid number. Try again.")

def calculate_gpa(grades):
    return round(sum(grades) / len(grades), 2)

def analyze_semester(grades):
    while True:
        choice = input("Which semester do you want to analyze?\n1. First half\n2. Second half\nEnter 1 or 2: ")
        if choice == "1":
            semester = grades[:len(grades)//2]
            break
        elif choice == "2":
            semester = grades[len(grades)//2:]
            break
        else:
            print(" Please enter 1 or 2.")
    semester_gpa = calculate_gpa(semester)
    overall_gpa = calculate_gpa(grades)
    print(f"Semester GPA: {semester_gpa}")
    print(f"Overall GPA: {overall_gpa}")
    if semester_gpa > overall_gpa:
        print("You're improving!")
    elif semester_gpa < overall_gpa:
        print("Looks like things slipped a bit no suprise.")
    else:
        print("➖ You've been consistent.")

def goal_gpa_check(grades, current_gpa):
    while True:
        try:
            goal = float(input("What’s your goal GPA? (0.0–4.0): "))
            if 0.0 <= goal <= 4.0:
                break
            else:
                print(" That goal is out of range.")
        except ValueError:
            print(" Invalid input.")
    
    if current_gpa >= goal:
        print(" You've already met your goal GPA. how suprising!")
        return
    
    possible = False
    for i in range(len(grades)):
        new_grades = grades.copy()
        new_grades[i] = 4.0
        new_gpa = calculate_gpa(new_grades)
        if new_gpa >= goal:
            print(f" If you raise grade {i+1} to 4.0, your GPA would be {new_gpa}")
            possible = True
    if not possible:
        print(" You'll need to improve more than one grade to reach your goal.")

# --- Main Program ---

print("4Welcome to the Overly Verbose GPA Calculator 🎓")

while True:
    try:
        num_classes = int(input("How many classes are you in smarty? "))
        if num_classes >= 5:
            break
        else:
            print(" i knew you couldnt handle 5 classes.")
    except ValueError:
        print("Please enter a valid number.")

grades = [get_valid_grade(i) for i in range(num_classes)]

current_gpa = calculate_gpa(grades)
print(f"\n Your current GPA is supprisingly: {current_gpa}\n")

analyze_semester(grades)

goal_gpa_check(grades, current_gpa)
