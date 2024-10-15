import datetime

def get_day_of_week(date_string):
    """
    Returns the day of the week for a given date string.

    Args:
        date_string: The date string in YYYY-MM-DD format.

    Returns:
        The day of the week as a string (e.g., "Monday", "Tuesday").
    """
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    day_of_week = date_object.strftime("%A")
    return day_of_week

# Get date input from the user
date_string = input("Enter a date in YYYY-MM-DD format: ")

# Calculate and print the day of the week
day = get_day_of_week(date_string)
print(f"The day of the week for {date_string} is {day}.")
