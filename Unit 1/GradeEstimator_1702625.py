import json

tasks_json = {
    "homeworkTypes": [
        {
            "name": "Discussions",
            "displayName": "Group Discussions",
            "numberOfTasksPerSemester": 8,
            "maximumPointsPerSubmission": 50
        },
        {
            "name": "Core Assessment",
            "displayName": "Core Assessments",
            "numberOfTasksPerSemester": 4,
            "maximumPointsPerSubmission": 50
        },
        {
            "name": "Course Project",
            "displayName": "Course Project",
            "numberOfTasksPerSemester": 8,
            "maximumPointsPerSubmission": 50
        }
    ]
}

with open("tasks.json", "w") as file:
    json.dump(tasks_json, file, indent=4)

print("tasks.json created successfully!")

import csv  # Import the module for creating CSV files.

# Enter the grades for all eight units.
data = [
    ["type", "Week1", "Week2", "Week3", "Week4",
     "Week5", "Week6", "Week7", "Week8"],
    ["discussion", 50, 50, 50, 50, 50, 50, 50, 50],
    ["course_project", 50, 50, 45, 50, 50, 45, 25, 50],
    ["core_assessment", 50, None, 50, None, 50, None, 50, None]
]

# Create the scenario where the final Unit 8 grades are zero.
grades_0 = [row.copy() for row in data]
grades_0[1][8] = 0  # Set Unit 8 discussion to zero.
grades_0[2][8] = 0  # Set Unit 8 course project to zero.

# Save the zero-grade scenario.
with open("grades_0.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_0)

# Create the scenario where the final Unit 8 grades are 50.
grades_50 = [row.copy() for row in data]
grades_50[1][8] = 50  # Set Unit 8 discussion to 50.
grades_50[2][8] = 50  # Set Unit 8 course project to 50.

# Save the 50-point scenario.
with open("grades_50.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_50)

# Confirm that both files were created.
print("grades_0.csv created successfully!")
print("grades_50.csv created successfully!")

import csv  # Import tools for reading CSV files.
import json  # Import tools for reading JSON files.

grades_filename = "grades_0.csv"  # Select the zero-grade scenario.

with open("tasks.json", "r") as tasks_file:  # Open the task properties.
    tasks_data = json.load(tasks_file)  # Load the task properties from JSON.

with open(grades_filename, "r", newline="") as grades_file:  # Open the selected grades.
    reader = csv.DictReader(grades_file)  # Read grades using the column headings.
    grades_data = list(reader)  # Store the grade rows.

grades_by_type = {row["type"]: row for row in grades_data}  # Index rows by task type.

task_name_mapping = {  # Match JSON names to CSV row names.
    "Discussions": "discussion",
    "Core Assessment": "core_assessment",
    "Course Project": "course_project"
}

total_points = 0  # Initialize the earned-points total.
maximum_points = 0  # Initialize the maximum-points total.

for task in tasks_data["homeworkTypes"]:  # Process each homework type.
    task_name = task["name"]  # Get the task name from JSON.
    task_count = task["numberOfTasksPerSemester"]  # Get the number of tasks.
    points_per_task = task["maximumPointsPerSubmission"]  # Get points per task.

    maximum_points += task_count * points_per_task  # Add the maximum possible points.

    csv_key = task_name_mapping[task_name]  # Find the corresponding CSV row.
    grade_row = grades_by_type[csv_key]  # Retrieve that row's grades.

    for column_name, grade_value in grade_row.items():  # Examine every grade cell.
        if column_name == "type":  # Skip the task-name column.
            continue

        if grade_value is None or grade_value.strip() == "":  # Check for blank grades.
            continue  # Ignore assignments that have not been graded.

        total_points += float(grade_value)  # Add the entered grade to the total.

percentage = total_points / maximum_points * 100  # Calculate the percentage.

if percentage > 90:  # Check the A threshold.
    letter_grade = "A"
elif percentage > 80:  # Check the B threshold.
    letter_grade = "B"
elif percentage > 70:  # Check the C threshold.
    letter_grade = "C"
elif percentage > 60:  # Check the D threshold.
    letter_grade = "D"
else:  # Handle 60 percent or lower.
    letter_grade = "F"

print(f"You have {total_points:g} out of {maximum_points}")  # Display the points.
print(f"Your percentage is {percentage:.2f}".rstrip("0").rstrip("."))  # Display percentage.
print(f"Your letter grade is: {letter_grade}")  # Display the letter grade.

import csv  # Import tools for reading CSV files.
import json  # Import tools for reading JSON files.

grades_filename = "grades_50.csv"  # Select the zero-grade scenario.

with open("tasks.json", "r") as tasks_file:  # Open the task properties.
    tasks_data = json.load(tasks_file)  # Load the task properties from JSON.

with open(grades_filename, "r", newline="") as grades_file:  # Open the selected grades.
    reader = csv.DictReader(grades_file)  # Read grades using the column headings.
    grades_data = list(reader)  # Store the grade rows.

grades_by_type = {row["type"]: row for row in grades_data}  # Index rows by task type.

task_name_mapping = {  # Match JSON names to CSV row names.
    "Discussions": "discussion",
    "Core Assessment": "core_assessment",
    "Course Project": "course_project"
}

total_points = 0  # Initialize the earned-points total.
maximum_points = 0  # Initialize the maximum-points total.

for task in tasks_data["homeworkTypes"]:  # Process each homework type.
    task_name = task["name"]  # Get the task name from JSON.
    task_count = task["numberOfTasksPerSemester"]  # Get the number of tasks.
    points_per_task = task["maximumPointsPerSubmission"]  # Get points per task.

    maximum_points += task_count * points_per_task  # Add the maximum possible points.

    csv_key = task_name_mapping[task_name]  # Find the corresponding CSV row.
    grade_row = grades_by_type[csv_key]  # Retrieve that row's grades.

    for column_name, grade_value in grade_row.items():  # Examine every grade cell.
        if column_name == "type":  # Skip the task-name column.
            continue

        if grade_value is None or grade_value.strip() == "":  # Check for blank grades.
            continue  # Ignore assignments that have not been graded.

        total_points += float(grade_value)  # Add the entered grade to the total.

percentage = total_points / maximum_points * 100  # Calculate the percentage.

if percentage > 90:  # Check the A threshold.
    letter_grade = "A"
elif percentage > 80:  # Check the B threshold.
    letter_grade = "B"
elif percentage > 70:  # Check the C threshold.
    letter_grade = "C"
elif percentage > 60:  # Check the D threshold.
    letter_grade = "D"
else:  # Handle 60 percent or lower.
    letter_grade = "F"

print(f"You have {total_points:g} out of {maximum_points}")  # Display the points.
print(f"Your percentage is {percentage:.2f}".rstrip("0").rstrip("."))  # Display percentage.
print(f"Your letter grade is: {letter_grade}")  # Display the letter grade.
