# Enter first name so the program can personalize the greeting.

first_name = input("Enter your first name: ")

# Enter last name so the program can personalize the greeting.

last_name = input("Enter your last name: ")

# Remove spaces from the beginning and end of the first name and capitalize only its first letter.

first_name = first_name.strip().capitalize()

# Remove spaces from the beginning and end of the last name and capitalize only its first letter.

last_name = last_name.strip().capitalize()

# Display the formatted greeting using the last name first, followed by the first name.

print("Hello " + last_name + ", " + first_name)

# Store the points received for the Unit 1 discussion assignment.

Unit1_discussion_points = 50

# Store the points received for the Unit 1 course project assignment.

Unit1_course_project_points = 50

# Store the points received for the Unit 1 core assessment assignment.

Unit1_core_assesment_points = 50

# Store the points received or expected for the Unit 2 discussion assignment.

Unit2_discussion_points = 49

# Store the points received or expected for the Unit 2 course project assignment.

Unit2_course_project_points = 49

# Store the maximum number of points possible for each individual assignment.

task_maximum_points = 50

# Create a list containing the discussion points earned for Units 1 and 2.

total_discussion_points = [Unit1_discussion_points, Unit2_discussion_points]

# Create a list containing the course project points earned for Units 1 and 2.

total_course_project_points = [Unit1_course_project_points, Unit2_course_project_points]

total_core_assessment_points = [Unit1_core_assesment_points]

# Add all discussion points from the list to calculate the current discussion total.

current_discussion_points = sum(total_discussion_points)

# Add all course project points from the list to calculate the current course project total.

current_course_project_points = sum(total_course_project_points)

# Add all core assessment points from the list to calculate the current core assessment total.

current_core_assessment_points = sum(total_core_assessment_points)

# Calculate the maximum possible points for all eight discussion assignments.

maximum_discussion_points = 8 * task_maximum_points

# Calculate the maximum possible points for all eight course project assignments.

maximum_course_project_points = 8 * task_maximum_points

# Calculate the maximum possible points for all four core assessment assignments.

maximum_core_assessment_points = 4 * task_maximum_points

# Display the current discussion points and maximum possible discussion points using formatted strings.

print(f"Currently you have {current_discussion_points} points for discussions out of {maximum_discussion_points}")

# Display the current course project points and maximum possible course project points using formatted strings.

print(f"Currently you have {current_course_project_points} points for course projects out of {maximum_course_project_points}")

# Display the current core assessment points and maximum possible core assessment points using formatted strings.

print(f"Currently you have {current_core_assessment_points} points for core assessments out of {maximum_core_assessment_points}")
