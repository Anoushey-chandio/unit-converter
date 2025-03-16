import streamlit as st  # Import Streamlit for creating the web-based UI

# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g., temperature conversion), call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined


# Streamlit UI setup
st.set_page_config(page_title="Unit Converter", page_icon="⚙️", layout="centered")  # Page setup
st.title("⚙️ Simple Unit Converter")  # Set title for the web app

# Add some description about the app
st.markdown("""
    This is a simple app that helps you convert between various units.  
    Enter a value, select the units to convert from and to, and hit 'Convert'.
""")

# Adding a sidebar with instructions and an app logo (optional)
st.sidebar.header("Instructions")
st.sidebar.write("""
    - Enter the numerical value to be converted.
    - Select the unit you want to convert from and the unit to convert to.
    - Press the **Convert** button to get the result.
""")

# User input: numerical value to convert
value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms"], index=0
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"], index=1)

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    if isinstance(result, str):
        st.error(result)  # Show error if conversion is not supported
    else:
        st.success(f"Converted Value: {result:.2f}")  # Display result with 2 decimal places