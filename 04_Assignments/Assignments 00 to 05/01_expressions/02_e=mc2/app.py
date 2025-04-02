# e=mc2 Calculator
import streamlit as st

# Pagr Layout
st.set_page_config(page_title="e=mc2 Calculator", page_icon="⚡")
st.title("⚡ e=mc2 Calculator")
st.sidebar.header("Instructions")
st.sidebar.info("This calculator is used to calculate the energy of a particle based on its mass and speed.")

# Defining Constant
c = 299792458  # Speed of light in m/s

# Mass Input
mass_in_kg = st.number_input("Enter the mass of the particle in kg", min_value=0.0, step=0.1)

# Energy Calculation
if mass_in_kg > 0:
    energy_in_joules = mass_in_kg * c ** 2
    st.write("e = m * C²...")
    st.write(f"m = {mass_in_kg} kg")
    st.write(f"C = {c} m/s")
    st.success(f"The energy is {energy_in_joules} joules!")
else:
    st.warning("Please enter a valid mass value.")