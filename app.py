
!pip install streamlit==1.28.1
import streamlit as st

def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero error!"

# Set the title of the app
st.title("Simple Calculator")

# Get input from the user
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Calculate the result
result = calculate(operation, num1, num2)

# Display the result
st.write(f"Result: {result}")


