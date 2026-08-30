# Ask the user to enter first name and save the answer in the first_name variable.
first_name = input("Enter your first name: ")

# Ask the user to enter last name and save the answer in the last_name variable.
last_name = input("Enter your last name: ")

# Ask the user to enter first name so the program can personalize the greeting.
first_name = input("Enter your first name: ")

# Ask the user to enter last name so the program can personalize the greeting.
last_name = input("Enter your last name: ")

# Remove spaces from the beginning and end of the first name and capitalize only its first letter.
first_name = first_name.strip().capitalize()

# Remove spaces from the beginning and end of the last name and capitalize only its first letter.
last_name = last_name.strip().capitalize()

# Display the formatted greeting using the last name first, followed by the first name.
print("Hello " + last_name + ", " + first_name)

# Store the points received for the Unit 1 discussion assignment.
Unit1_discussion_points = 49

# Store the points received or expected for the Unit 1 course project assignment.
Unit1_course_project_points = 50

# Store the points received or expected for the Unit 1 core assessment assignment.
Unit1_core_assesment_points = 50

# Store the maximum number of points possible for each individual task.
task_maximum_points = 50

# Add the points from all three Unit 1 assignments to calculate the total points earned.
total_points = Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assesment_points

# Display the total number of points earned for Unit 1.
print("Total Points:", total_points)

# Compare the discussion points with the maximum possible points and display True or False.
print("Got maximum points for Unit 1 discussion?", Unit1_discussion_points == task_maximum_points)

# Compare the course project points with the maximum possible points and display True or False.
print("Got maximum points for Unit 1 course project?", Unit1_course_project_points == task_maximum_points)

# Compare the core assessment points with the maximum possible points and display True or False.
print("Got maximum points for Unit 1 core assessment?", Unit1_core_assesment_points == task_maximum_points)
