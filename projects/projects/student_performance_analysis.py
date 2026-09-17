# Student Performance Analysis
# Using Pandas

import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("=" * 50)
print("       STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

# Display dataset
print("\nDataset:")
print(df)

# Basic information
print("\nDataset Information:")
print(df.info())

# Calculate average marks
subjects = ["Python", "Maths", "English"]

df["Average"] = df[subjects].mean(axis=1)

# Calculate total marks
df["Total"] = df[subjects].sum(axis=1)

# Grade calculation
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(calculate_grade)

# Pass/Fail
df["Status"] = df["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Display final analysis
print("\nFinal Analysis:")
print(df)

# Top performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print(top_student[["Name", "Average", "Grade"]])

# Class statistics
print("\nClass Statistics:")
print(f"Class Average: {df['Average'].mean():.2f}")
print(f"Highest Average: {df['Average'].max():.2f}")
print(f"Lowest Average: {df['Average'].min():.2f}")

print("\n" + "=" * 50)
print("Analysis Completed Successfully")
print("=" * 50)
