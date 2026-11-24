
import sys


def calculate_grade(average):
    if average >= 90:
        return "S"
    if average >= 80:
        return "A"
    if average >= 65:
        return "B"
    if average >= 50:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def get_student():
    """Args > interactive input > sample data (for Jenkins/Docker, no keyboard)."""
    # python Student.py SUDARSHAN BCA 3 Python 85 DBMS 78 Computer 82
    if len(sys.argv) == 10:
        a = sys.argv[1:]
        subjects = [a[3], a[5], a[7]]
        marks = [float(a[4]), float(a[6]), float(a[8])]
        return a[0], a[1], a[2], subjects, marks
    if sys.stdin.isatty():
        name = input("Enter name: ")
        dept = input("Enter department: ")
        sem = input("Enter semester: ")
        subjects, marks = [], []
        for i in (1, 2, 3):
            subjects.append(input(f"Enter subject {i} name: "))
            marks.append(float(input(f"Enter marks in {subjects[-1]}: ")))
        return name, dept, sem, subjects, marks
    return "SUDARSHAN", "BCA", "3", ["Python", "DBMS", "Computer"], [85, 78, 82]


def main():
    name, dept, sem, subjects, marks = get_student()
    average = sum(marks) / 3
    print("===== Student Details =====")
    print(f"Name       : {name}")
    print(f"Department : {dept}")
    print(f"Semester   : {sem}")
    for sub, m in zip(subjects, marks):
        print(f"{sub:<11}: {m:g}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {calculate_grade(average)}")


if __name__ == "__main__":
    main()
