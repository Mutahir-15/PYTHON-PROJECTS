# Seconds in year
import streamlit as st

#Page layout
st.set_page_config(page_title="Seconds in year", page_icon=":tada:")
st.title("Seconds in a Year Calculator")
st.sidebar.header("Instruction")
st.sidebar.info("This is a simple app to calculate the number of seconds in a year.")

#Constant for conversions
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

# Set the title of the app

# Display a brief description
st.write("Click the button below to calculate the number of seconds in a non-leap year (365 days).")

# Calculate and display the result when the user clicks a button
if st.button("Calculate Seconds"):
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    st.write("Days per Year:", DAYS_PER_YEAR)
    st.write("Hours per Day:", HOURS_PER_DAY)
    st.write("Minutes per Hour:", MIN_PER_HOUR)
    st.write("Seconds per Minute:", SEC_PER_MIN)
    st.write(F"Formula: **{DAYS_PER_YEAR} * {HOURS_PER_DAY} * {MIN_PER_HOUR} * {SEC_PER_MIN}**")
    st.success(f"There are **{total_seconds:,}** seconds in a year!")