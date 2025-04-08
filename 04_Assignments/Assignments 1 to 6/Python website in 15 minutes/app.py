# Python website powered by AI. As an Innovation I decided to add Gemini's API as a bonus..❤
import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Set the page configuration and main title
st.set_page_config(page_title="AI Website Powered by Gemini API")
st.title("Kindness Idea Generator Powered by AI")

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key exists
if not GEMINI_API_KEY:
    st.error("Error: GEMINI_API_KEY not found in .env file. Please set the API key and try again.")
    st.stop()

# Configure the Gemini API with the retrieved key
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')  # Set up the model
except Exception as e:
    st.error(f"Error: Failed to configure Gemini API. {str(e)}")
    st.stop()

# Define a dictionary containing focus areas and related global issues
KINDNESS_DATA = {
    "Support Local Parks": [
        "Littering in Community Parks",
        "Lack of Play Equipment for Kids",
        "Overgrown Trails and Pathways"
    ],
    "Help Neighbors": [
        "Elderly Neighbors Living Alone",
        "Families Struggling with Childcare",
        "New Residents Feeling Isolated"
    ],
    "Spread Positivity": [
        "Low Community Spirit at Events",
        "Negative Graffiti in Public Spaces",
        "Lack of Community Appreciation Days"
    ],
    "Promote Education": [
        "Underfunded Local Schools",
        "Lack of After-School Programs",
        "Limited Access to School Supplies"
    ],
    "Fight Hunger Locally": [
        "Food Insecurity in Low-Income Areas",
        "Lack of Community Gardens",
        "Underutilized Food Donation Drives"
    ],
    "Support Local Healthcare": [
        "Overcrowded Local Clinics",
        "Lack of Mental Health Resources",
        "Low Awareness of Free Health Services"
    ],
    "Encourage Equality": [
        "Discrimination in Local Hiring Practices",
        "Inaccessible Public Spaces for Disabled Residents",
        "Lack of Diversity in Community Events"
    ],
    "Protect Local Wildlife": [
        "Urban Sprawl Affecting Local Birds",
        "Pollution in Nearby Streams",
        "Stray Animals Needing Care"
    ],
    "Reduce Poverty Locally": [
        "High Unemployment in the Community",
        "Homelessness on Main Streets",
        "Lack of Job Training Programs"
    ],
    "Promote Peace in the Community": [
        "Tensions Between Neighborhood Groups",
        "Youth Conflicts at Local Hangouts",
        "Noise Complaints Disrupting Harmony"
    ],
    "Support Local Families": [
        "Single Parents Needing Support",
        "Families Facing Utility Shutoffs",
        "Lack of Affordable Family Activities"
    ],
    "Encourage Sustainability": [
        "Excessive Waste at Local Events",
        "Limited Recycling Options in the Area",
        "Energy Overuse in Community Buildings"
    ],
    "Raise Awareness Locally": [
        "Low Voter Turnout in Local Elections",
        "Unreported Safety Hazards in Public Areas",
        "Lack of Awareness About Local Resources"
    ],
    "Support Local Businesses": [
        "Small Shops Struggling to Compete",
        "Decline in Farmers' Market Attendance",
        "Lack of Promotion for Local Artisans"
    ],
    "Foster Creativity in the Community": [
        "Limited Art Classes for Kids",
        "Lack of Public Art Installations",
        "Underused Community Theater Spaces"
    ]
}

# Initialize variables in session state
if "selected_focus" not in st.session_state:
    st.session_state.selected_focus = None
if "current_issue" not in st.session_state:
    st.session_state.current_issue = None
if "current_action" not in st.session_state:
    st.session_state.current_action = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

st.write("""
### What This Program Does
This app helps you make a positive impact in your local community through AI-generated acts of kindness:
- Select a focus area (e.g., 'Support Local Parks') from the dropdown in the sidebar.
- Click 'Generate Idea' to see a local community issue and a kindness action generated by the Gemini 2.0 API.
- The app acts as an intelligent agent, choosing an issue and generating an action that align with your focus.
- Click 'Generate Idea' again to see a new suggestion for the same focus area.
- Click 'Reset' to start over with a new focus area.
- Let's make our community a better place, one kind act at a time!
""")

# Sidebar input section
with st.sidebar:
    st.header("Kindness Generator Controls")
    focus = st.selectbox("Select your focus area:", options=["Choose a focus area..."] + list(KINDNESS_DATA.keys()))
    generate_button = st.button("Generate Idea")
    reset_button = st.button("Reset")

# Logic to generate kindness ideas using AI
if generate_button:
    if focus == "":
        st.warning("Please select a focus area.")
    else:
        st.session_state.selected_focus = focus
        issue = random.choice(KINDNESS_DATA[focus])
        st.session_state.current_issue = issue
        
        # Generate action using Gemini AI
        try:
            prompt = f"Suggest a small, actionable act of kindness to address the local community of Pakistan issue: {issue}. Keep it simple, practical, and relevant to a local neighborhood or city context."
            response = model.generate_content(prompt)
            action = response.text.strip()
            st.session_state.current_action = action
        except Exception as e:
            st.session_state.current_action = f"Error: Could not generate action. {str(e)}"
        
        st.session_state.results_shown = True

# Logic to reset the app state
if reset_button:
    st.session_state.selected_focus = None
    st.session_state.current_issue = None
    st.session_state.current_action = None
    st.session_state.results_shown = False
    st.rerun()

# Display the final output
if st.session_state.results_shown:
    st.write("### Kindness Idea")
    st.markdown(f"**Issue:** {st.session_state.current_issue}")
    if "Error" in st.session_state.current_action:
        st.error(st.session_state.current_action)
    else:
        st.success(f"**Action:** {st.session_state.current_action}")
    st.write("Let's make a difference, one kind act at a time!")
