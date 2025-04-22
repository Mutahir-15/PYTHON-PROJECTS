# Leap year
import streamlit as st

# Set the title of the app
st.title("Leap Year Checker")

# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "That's a leap year!"
            else:
                return "That's not a leap year."
        else:
            return "That's a leap year!"
    else:
        return "That's not a leap year."

# Explanation of the program
st.write("""
### What This Program Does
This program checks if a given year is a leap year according to the Gregorian calendar rules:
1. The year must be evenly divisible by 4.
2. If the year is divisible by 100, it is **not** a leap year, unless:
3. The year is also divisible by 400, then it **is** a leap year.

Enter a year in the sidebar and click 'Check Year' to see the result.
""")

# Add the year input to the sidebar
with st.sidebar:
    st.header("Input a Year")
    year = st.number_input("Please input a year:", min_value=0, max_value=9999, value=2020, step=1)

# Button to check if it's a leap year
if st.button("Check Year"):
    if year < 0:
        st.error("Please enter a valid year (0 or greater).")
    else:
        result = is_leap_year(year)
        st.write("### Result")
        # Style the output: green for leap year, red for non-leap year
        if "leap year" in result:
            st.success(result)
        else:
            st.warning(result)