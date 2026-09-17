import pandas as pd
import matplotlib.pyplot as plt

# Student Performance Analyzer

students = {
    "Rahul": [78, 85, 92],
    "Priya": [88, 76, 90],
    "Aman": [65, 72, 68],
    "Neha": [95, 91, 94]
}

print("=" * 45)
print("       STUDENT PERFORMANCE ANALYZER")
print("=" * 45)

for name, marks in students.items():

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    status = "Pass" if average >= 40 else "Fail"

    print(f"\nStudent: {name}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

print("\n" + "=" * 45)
print("Analysis Completed")
print("=" * 45)
# Subject-wise Average
print("\nSubject-wise Average Marks:")

for subject in subjects:
    print(f"{subject}: {df[subject].mean():.2f}")

# Attendance Analysis
print("\nAttendance Analysis:")
print(f"Average Attendance: {df['Attendance'].mean():.2f}%")

# Students with high attendance
high_attendance = df[df["Attendance"] >= 90]

print("\nStudents with Attendance >= 90%:")
print(high_attendance[["Name", "Attendance"]])

# Grade Distribution
print("\nGrade Distribution:")
print(df["Grade"].value_counts())

print("\nAnalysis Completed Successfully!")
# Student-wise Average Marks Chart

plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Average"])

plt.title("Student-wise Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
