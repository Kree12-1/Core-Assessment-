# Import the requests library so that we can make a web request to the World Time API.
import requests

# Import datetime so we can convert the Unix timestamp into a Python date/time object.
from datetime import datetime

# Store the World Time API URL for the America/Chicago timezone.
url = "https://time.now/developer/api/timezone/America/Chicago"

# This line sends a GET request to the TimeAPI website so the program can retrieve the current date and time..
response = requests.get(url)

# This line converts the API response into a Python dictionary so the program can access the returned information.
data = response.json()

# Get the client's IP address from the JSON response.
client_ip = data["client_ip"]

# Get the current day of the year from the JSON response.
day_of_year = data["day_of_year"]

# Get the current UTC date and time from the JSON response.
utc_datetime = data["utc_datetime"]

# Display the client's IP address.
print("Client IP:", client_ip)

# Display the current day of the year returned by the API.
print("Day of year:", day_of_year)

# Display the current UTC date and time returned by the API.
print("UTC datetime:", utc_datetime)

# Store the date when the course began and convert it to the day of the year.
# Change this date to the actual first day of your course if necessary.
begin_course_day = datetime(2026, 8, 17).timetuple().tm_yday

# Get the Unix timestamp from the JSON response and convert it to a datetime object.
now_date = datetime.fromtimestamp(data["unixtime"])

# Convert the current datetime into the day of the year.
now_day = now_date.timetuple().tm_yday

# Calculate how many days have passed since the course began.
days_completed = now_day - begin_course_day

# Divide the number of completed days by 7 because there are 7 days in one Unit.
# int() removes any decimal portion from the result.
units_completed = int(days_completed / 7)

# Display the current Unit of the class out of 8 total Units.
print(f"You have completed {units_completed} Units of 8.")
