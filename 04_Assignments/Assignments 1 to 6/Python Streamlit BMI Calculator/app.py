# BMI Calculator 
import streamlit as st

# Page layout
st.set_page_config(page_title="BMI Calculator", page_icon=":bar_chart:")
st.title("BMI Calculator")

# Initialize session state
if "bmi" not in st.session_state:
    st.session_state.bmi = None
if "category" not in st.session_state:
    st.session_state.category = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Explanation
st.write("""
### What This Program Does
This app calculates your Body Mass Index (BMI) based on your weight and height:
- Enter your weight in kilograms (kg) and height in meters (m) in the sidebar.
- Click 'Calculate BMI' to see your BMI and weight category.
- BMI is calculated as: weight (kg) / (height (m)²).
- The app will categorize your BMI:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 ≤ BMI < 25
  - Overweight: 25 ≤ BMI < 30
  - Obese: BMI ≥ 30
- Click 'Reset' to clear the results and start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("BMI Calculator Inputs")
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, value=70.0, step=0.1)
    height = st.number_input("Enter your height (m):", min_value=0.1, value=1.75, step=0.01)
    calculate_button = st.button("Calculate BMI")
    reset_button = st.button("Reset")

# Function to calculate BMI and determine category
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)  # Round to 2 decimal places
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Handle the calculate button
if calculate_button:
    if height == 0:
        st.session_state.feedback = "Error: Height cannot be zero."
        st.session_state.results_shown = True
        st.error(st.session_state.feedback)
    else:
        bmi, category = calculate_bmi(weight, height)
        st.session_state.bmi = bmi
        st.session_state.category = category
        st.session_state.results_shown = True
        st.write("### Result")
        st.write(f"Your BMI is: **{bmi}**")
        if category == "Normal weight":
            st.success(f"Category: {category}")
        else:
            st.warning(f"Category: {category}")

# Handle the reset button
if reset_button:
    st.session_state.bmi = None
    st.session_state.category = None
    st.session_state.results_shown = False
    st.rerun()

# Display the result if it exists
if st.session_state.results_shown and not calculate_button:
    st.write("### Result")
    st.write(f"Your BMI is: **{st.session_state.bmi}**")
    if st.session_state.category == "Normal weight":
        st.success(f"Category: {st.session_state.category}")
    else:
        st.warning(f"Category: {st.session_state.category}")