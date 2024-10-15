import streamlit as st
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

# Set the title of the app
st.title("Day of the Week Calculator")

# Get date input from the user
date_string = st.text_input("Enter a date in YYYY-MM-DD format (e.g., 2024-03-15):")

# Calculate and display the day of the week
if date_string:
    try:
        day = get_day_of_week(date_string)
        st.write(f"The day of the week for {date_string} is {day}.")
    except ValueError:
        st.error("Invalid date format. Please use YYYY-MM-DD.")
