# Ask the user to enter first name so the program can personalize the greeting.
first_name = input("Enter your first name: ")

# Ask the user to enter last name so the program can personalize the greeting.
last_name = input("Enter your last name: ")

# Remove extra spaces and capitalize the first letter of the first name.
first_name = first_name.strip().capitalize()

# Remove extra spaces and capitalize the first letter of the last name.
last_name = last_name.strip().capitalize()

# Display the user's last name followed by their first name.
print("Hello " + last_name + ", " + first_name)


# Create a class to store information about discussion assignments.
class Discussions:
    # Set the maximum points possible for one discussion assignment.
    maximum_points_per_task = 50

    # Set the number of discussion assignments required during the semester.
    tasks_per_semester = 8

    # Set the name of the assignment type for display messages.
    display_name = "discussion"


# Create a class to store information about course project assignments.
class Course_projects:
    # Set the maximum points possible for one course project assignment.
    maximum_points_per_task = 50

    # Set the number of course project assignments required during the semester.
    tasks_per_semester = 8

    # Set the name of the assignment type for display messages.
    display_name = "course project"


# Create a class to store information about core assessment assignments.
class Core_assesments:
    # Set the maximum points possible for one core assessment assignment.
    maximum_points_per_task = 50

    # Set the number of core assessment assignments required during the semester.
    tasks_per_semester = 4

    # Set the name of the assignment type for display messages.
    display_name = "core assessment"


# Store the Unit 1 discussion grade.
Unit1_discussion_points = 50

# Store the Unit 2 discussion grade.
Unit2_discussion_points = 50

# Store the Unit 3 discussion grade using the maximum points from the Discussions class.
Unit3_discussion_points = Discussions.maximum_points_per_task


# Store the Unit 1 course project grade.
Unit1_course_project_points = 50

# Store the Unit 2 course project grade.
Unit2_course_project_points = 50

# Store the Unit 3 course project grade.
Unit3_course_project_points = 45


# Store the Unit 1 core assessment grade.
Unit1_core_assessment_points = 50

# Store the Unit 3 core assessment grade using the maximum points from the Core_assesments class.
Unit3_core_assessment_points = Core_assesments.maximum_points_per_task


# Create a list containing all discussion grades received so far.
total_discussion_points = [
    Unit1_discussion_points,
    Unit2_discussion_points,
    Unit3_discussion_points
]

# Create a list containing all course project grades received so far.
total_course_project_points = [
    Unit1_course_project_points,
    Unit2_course_project_points,
    Unit3_course_project_points
]

# Create a list containing all core assessment grades received so far.
total_core_assessment_points = [
    Unit1_core_assessment_points,
    Unit3_core_assessment_points
]


# Add all discussion grades together to calculate the current discussion total.
current_discussion_points = sum(total_discussion_points)

# Add all course project grades together to calculate the current course project total.
current_course_project_points = sum(total_course_project_points)

# Add all core assessment grades together to calculate the current core assessment total.
current_core_assessment_points = sum(total_core_assessment_points)


# Calculate the maximum possible discussion points for the assignments completed so far.
maximum_discussion_points = len(total_discussion_points) * Discussions.maximum_points_per_task

# Calculate the maximum possible course project points for the assignments completed so far.
maximum_course_project_points = len(total_course_project_points) * Course_projects.maximum_points_per_task

# Calculate the maximum possible core assessment points for the assignments completed so far.
maximum_core_assessment_points = len(total_core_assessment_points) * Core_assesments.maximum_points_per_task


# Display the current discussion points using the required .format() method.
print("Currently you have {} points for discussions out of {}".format(
    current_discussion_points,
    maximum_discussion_points
))

# Display the current course project points using the required .format() method.
print("Currently you have {} points for course projects out of {}".format(
    current_course_project_points,
    maximum_course_project_points
))

# Display the current core assessment points using the required .format() method.
print("Currently you have {} points for core assessments out of {}".format(
    current_core_assessment_points,
    maximum_core_assessment_points
))


# Create a function to determine whether all assignments received maximum points.
def check_maximum_points(points_list, assignment_type):
    # Assume all assignments received maximum points at the beginning.
    received_maximum_points = True

    # Loop through every grade in the list.
    for points in points_list:
        # Check whether the current grade is less than the maximum possible points.
        if points < assignment_type.maximum_points_per_task:
            # Change the result to False because at least one grade was below maximum.
            received_maximum_points = False

    # Check whether every assignment received maximum points.
    if received_maximum_points:
        # Display the congratulations message using the .format() method.
        print("Congrats! You got maximum points for ALL {} homeworks so far!".format(
            assignment_type.display_name
        ))
    else:
        # Display the unsuccessful message using the .format() method.
        print("Unfortunately you did not get maximum points for ALL {} homeworks".format(
            assignment_type.display_name
        ))


# Check whether all discussion assignments received maximum points.
check_maximum_points(total_discussion_points, Discussions)

# Check whether all course project assignments received maximum points.
check_maximum_points(total_course_project_points, Course_projects)

# Check whether all core assessment assignments received maximum points.
check_maximum_points(total_core_assessment_points, Core_assesments)
