import csv

data = [
    ["type", "Week1", "Week2", "Week3", "Week4", "Week5", "Week6", "Week7", "Week8"],
    ["discussion", 50, 50, 50, -10, 50, 0, 50, 50],
    ["course_project", 100, 50, 45, 50, 50, 50, 50, 50],
    ["core_assessment", 50, None, 50, None, 50, None, 50, None]
]

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("grades.csv created successfully!")



from google.colab import files

files.download("grades.csv")



# Import pandas library because the program can read and work with the CSV file.
import pandas as pd

# Read the grades.csv file into a pandas DataFrame because file contains the grades for each type of homework.
grades = pd.read_csv("grades.csv")

# Display a message so the user knows that the original data is being shown.
print("Original Grades:")

# Display all of the information that was read from the CSV file.
print(grades)

# Display a message indicating that discussion grades will be shown.
print("Discussion Grades:")

# Select the row where the homework type is discussion and display it.
print(grades[grades["type"] == "discussion"])

# Display a grades for that Week 1 will be shown.
print("Week 1 Grades:")

# Display the homework type and Week 1 grade for every type of homework.
print(grades[["type", "Week1"]])

# Loop through every assignment type because every grade must be checked.
for index, row in grades.iterrows():

    # Get the assignment type from the CSV.
    assignment_type = row["type"]

    # Match the CSV assignment type to the appropriate JSON name.
    if assignment_type == "discussion":
        json_name = "Discussions"

    elif assignment_type == "course_project":
        json_name = "Course Project"

    elif assignment_type == "core_assessment":
        json_name = "Core Assessment"

    # Set the default maximum grade.
    max_grade = 50

    # Check every week's grade.
    for column in grades.columns[1:]:

        # Skip blank grades because there is no grade to clean.
        if pd.isna(grades.at[index, column]):
            continue

        # Change negative grades to zero.
        if grades.at[index, column] < 0:
            grades.at[index, column] = 0

        # Change grades above the maximum to the maximum allowed grade.
        if grades.at[index, column] > max_grade:
            grades.at[index, column] = max_grade

# Display the cleaned grades.
print("\nCleaned Grades")
print(grades)
