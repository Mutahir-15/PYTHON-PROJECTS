# Square Number Calculator
import streamlit as st

# Page Layout
st.set_page_config(page_title="Square Number Calculator", page_icon="🔢", layout="centered", initial_sidebar_state="expanded")
st.title("🔢 Square Number Calculator")
st.sidebar.header("Instructions")
st.sidebar.info("Enter a number and click the button to calculate its square.")

# Main Functionality
def calculate_square():
    number = st.number_input("Enter a number:", step=1.0)
    
    if st.button("Calculate Square"):
        square = number ** 2
        st.success(f"The square of {number} is {square}")

if __name__ == "__main__":
    calculate_square()