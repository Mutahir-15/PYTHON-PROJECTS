# Planetary Weight Calculator
import streamlit as st

# Page layout
st.set_page_config(page_title="Planetary Weight Calculator", page_icon="🌏")
st.title("Planetary Weight Calculator")

# Gravitational constants (relative to Earth's gravity)
PLANET_GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Initialize session state
for key in ["planetary_weight", "selected_planet", "earth_weight", "results_shown"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "results_shown" else False

# Description
st.write("""
### What This Program Does
Ever wondered how much you'd weigh on other planets?  
This tool calculates your weight on a selected planet based on your **Earth weight** in **kilograms (kg)**.

**How to use:**
- Enter your Earth weight in the sidebar.
- Pick a planet from the dropdown.
- Click **'Calculate Weight'** to see your weight on that planet.
- Click **'Clear'** to reset the form.

#### Gravitational Constants (Relative to Earth):
- Mercury: 37.6%
- Venus: 88.9%
- Mars: 37.8%
- Jupiter: 236.0%
- Saturn: 108.1%
- Uranus: 81.5%
- Neptune: 114.0%
""")

# Sidebar Input
with st.sidebar:
    st.header("Your Input")
    earth_weight = st.number_input("Your Earth weight (kg):", min_value=0.0, value=50.0, step=1.0)
    planet = st.selectbox("Select a planet:", [""] + list(PLANET_GRAVITY.keys()), index=3)
    calculate_btn = st.button("Calculate Weight")
    clear_btn = st.button("Clear")

# Handle calculation
if calculate_btn and planet:
    gravity = PLANET_GRAVITY[planet]
    result_weight = round(earth_weight * gravity, 2)

    st.session_state.earth_weight = earth_weight
    st.session_state.selected_planet = planet
    st.session_state.planetary_weight = result_weight
    st.session_state.results_shown = True

    st.write("### Result")
    st.success(f"Your weight on **{planet}** would be **{result_weight} kg**")

# Handle clear
if clear_btn:
    for key in ["planetary_weight", "selected_planet", "earth_weight"]:
        st.session_state[key] = None
    st.session_state.results_shown = False
    st.rerun()

# Show result if available
if st.session_state.results_shown and not calculate_btn:
    st.write("### Result")
    st.success(f"Your weight on **{st.session_state.selected_planet}** would be **{st.session_state.planetary_weight} kg**")