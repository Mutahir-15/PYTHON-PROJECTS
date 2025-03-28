import streamlit as st

# Page Layout
st.set_page_config(page_title="Triangle Perimeter Calculator", page_icon="📐", layout="centered")
st.title("📐 Triangle Perimeter Calculator")
st.sidebar.header("Instructions")
st.sidebar.info("Enter the lengths of the three sides of a triangle, then click the button to calculate its perimeter.")

def calculate_triangle_perimeter():
    side_a = st.number_input("Enter length of side A:", min_value=1.0, step=0.1)
    side_b = st.number_input("Enter length of side B:", min_value=1.0, step=0.1)
    side_c = st.number_input("Enter length of side C:", min_value=1.0, step=0.1)
    
    if st.button("Calculate Perimeter"):
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            perimeter = side_a + side_b + side_c
            st.success(f"The perimeter of the triangle is {perimeter}")
        else:
            st.error("Invalid triangle sides! The sum of any two sides must be greater than the third side.")

if __name__ == "__main__":
    calculate_triangle_perimeter()