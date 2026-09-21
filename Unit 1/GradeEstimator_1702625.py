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

import json # Import the json module to read the tasks.json file.

class Task_type: # Create the Task_type class.
    def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):

       # Create the constructor with four values.
        self.name = name
        self.display_name = display_name
        self.tasks_per_semester = tasks_per_semester
        self.maximum_points_per_task = maximum_points_per_task

with open("tasks.json", "r") as file: # Open the tasks.json file.
    task_data = json.load(file) # Read the JSON data.

task_types = [] # Create an empty list for the task types.

for task in task_data["homeworkTypes"]: # Go through each homework type.
    task_type = Task_type(
        task["name"],
        task["displayName"],
        task["numberOfTasksPerSemester"],
        task["maximumPointsPerSubmission"]
    )
    task_types.append(task_type) # Add the object to the list.

total_maximum_points = 0 # Start the total maximum points at zero.

for task_type in task_types: # Go through each task type in the list.
    total_maximum_points += (
        task_type.tasks_per_semester *
        task_type.maximum_points_per_task
    ) # Calculate the maximum points.

print("Maximum grade you can get for this class is:", total_maximum_points)
