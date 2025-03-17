import streamlit as st  # Import Streamlit for the web UI

# Function to convert units

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Create a key based on selected units
    if key in conversions:
        return value * conversions[key]  # Multiply value by conversion factor
    else:
        return "Conversion not supported"  # Show message if conversion is unavailable

# Set up the Streamlit page
st.set_page_config(page_title="Unit Converter", page_icon="⚙️", layout="centered")
st.title("⚙️ Simple Unit Converter")  # App title

# Description of the app
st.markdown("""
    This app helps you convert units. 
    Enter a value, select units, and press 'Convert'.
""")

# Sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
    - Enter a number.
    - Select the units to convert from and to.
    - Press **Convert** to get the result.
""")

# Input value from user
value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)

# Dropdowns to select units
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"], index=0)
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"], index=1)

# Button to perform conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if isinstance(result, str):
        st.error(result)  # Show error for unsupported conversions
    else:
        st.success(f"Converted Value: {result:.2f}")  # Show result rounded to 2 decimals
