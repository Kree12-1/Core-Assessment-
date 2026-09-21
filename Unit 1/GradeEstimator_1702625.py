# Import the json library because we need to read data from the tasks.json file.
import json


# Create the Task_type class because we need to store information about each task category.
class Task_type:

    # Create the constructor because each Task_type object needs initial values.
    def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):

        # Store the task name because we need to identify the task category.
        self.name = name

        # Store the display name because we need a readable task description.
        self.display_name = display_name

        # Store the number of tasks because we need it to calculate total points.
        self.tasks_per_semester = tasks_per_semester

        # Store the maximum points because we need it to calculate total points.
        self.maximum_points_per_task = maximum_points_per_task


# Open the tasks.json file because the program needs to read task information.
with open("tasks.json", "r") as file:

    # Convert the JSON data into a Python dictionary so it can be used.
    task_data = json.load(file)


# Create an empty list because we need to store all Task_type objects.
task_types = []


# Loop through each task in the JSON file because each task needs a class object.
for task in task_data["tasks"]:

    # Create a new Task_type object using values loaded from the JSON file.
    new_task = Task_type(
        task["name"],
        task["displayName"],
        task["numberOfTasksPerSemester"],
        task["maximumPointsPerSubmission"]
    )

    # Add the Task_type object to the list because we need all task types together.
    task_types.append(new_task)


# Create a variable starting at zero because we will add points from each task type.
total_maximum_points = 0


# Loop through each task object because we need to calculate all possible points.
for task in task_types:

    # Multiply tasks by points per task because this gives the total for this category.
    task_total_points = (
        task.tasks_per_semester *
        task.maximum_points_per_task
    )

    # Add the category total because we need the maximum grade for the whole class.
    total_maximum_points += task_total_points


# Display the maximum grade because the user needs to see the final calculation.
print("Maximum grade you can get for this class is:", total_maximum_points)
