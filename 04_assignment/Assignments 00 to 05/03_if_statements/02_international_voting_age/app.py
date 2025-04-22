# International Voting Age
import streamlit as st

# Constants for voting ages
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

# Page layout
st.set_page_config(page_title="International Voting Age Checker")
st.title("International Voting Age Checker")

# Explanation of the program
st.write("""
### What This Program Does
This program checks if you can vote in three fictional countries based on your age:
- **Peturksbouipo**: Voting age is 16 (like Scotland, Ethiopia, and Austria).
- **Stanlau**: Voting age is 25 (like the United Arab Emirates).
- **Mayengua**: Voting age is 48 (not a real voting age anywhere, as far as we know).
Enter your age in the sidebar and click 'Check Eligibility' to see the results.
""")

# Add the age input to the sidebar
with st.sidebar:
    st.header("Input Your Age")
    user_age = st.number_input("How old are you?", min_value=0, max_value=150, value=20, step=1)

# Button to check eligibility
if st.button("Check Eligibility"):
    if user_age < 0:
        st.error("Please enter a valid age (0 or greater).")
    else:
        st.write("### Voting Eligibility Results")
        
        if user_age >= PETURKSBOUIPO_AGE:
            message = f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}."
            st.markdown(f"<span style='color:green'>{message}</span>", unsafe_allow_html=True)
        else:
            message = f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}."
            st.markdown(f"<span style='color:red'>{message}</span>", unsafe_allow_html=True)

        if user_age >= STANLAU_AGE:
            message = f"You can vote in Stanlau where the voting age is {STANLAU_AGE}."
            st.markdown(f"<span style='color:green'>{message}</span>", unsafe_allow_html=True)
        else:
            message = f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}."
            st.markdown(f"<span style='color:red'>{message}</span>", unsafe_allow_html=True)
            
        if user_age >= MAYENGUA_AGE:
            message = f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}."
            st.markdown(f"<span style='color:green'>{message}</span>", unsafe_allow_html=True)
        else:
            message = f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}."
            st.markdown(f"<span style='color:red'>{message}</span>", unsafe_allow_html=True)