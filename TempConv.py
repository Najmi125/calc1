import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def main():
    st.title("Temperature Converter")

    # Dropdown to select temperature scale
    option = st.selectbox(
        "Select the input temperature scale:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )
    
    # Get input temperature based on the selected option
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:")
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is {fahrenheit:.2f}°F")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:")
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is {celsius:.2f}°C")

if __name__ == "__main__":
    main()
