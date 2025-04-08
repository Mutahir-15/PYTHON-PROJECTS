# Sentence Generator
import streamlit as st

# Page layout
st.set_page_config(page_title="Sentence Generator")
st.title("Sentence Generator")

# Initialize session state
if "sentence" not in st.session_state:
    st.session_state.sentence = ""
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to generate the sentence
def make_sentence(word, part_of_speech):

    if part_of_speech == 0:
        return f"I am excited to add this {word} to my vast collection of them!"
    elif part_of_speech == 1:
        return f"It's so nice outside today it makes me want to {word}!"
    elif part_of_speech == 2:
        return f"Looking out my window, the sky is big and {word}!"
    else:
        return "Please select a valid part of speech (0, 1, or 2)."

# Explanation of the program
st.write("""
### What This Program Does
This program helps you create a sentence based on a word and its part of speech.
- Enter a word (noun, verb, or adjective) in the sidebar.
- Choose the part of speech: 0 for noun, 1 for verb, 2 for adjective.
- Click 'Generate Sentence' to see the result.
- You can also click 'Clear' to start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Input for Sentence Generator")
    word = st.text_input("Enter a word (noun, verb, or adjective):", value="groovy")
    part_of_speech = st.selectbox("Select part of speech:", options=[0, 1, 2], format_func=lambda x: ["Noun (0)", "Verb (1)", "Adjective (2)"][x])
    generate_button = st.button("Generate Sentence")
    clear_button = st.button("Clear")

# Handle sentence generation
if generate_button:
    st.session_state.sentence = make_sentence(word, part_of_speech)
    st.session_state.results_shown = True
    st.write("### Result:")
    st.success(st.session_state.sentence)

# Handle clearing the input
if clear_button:
    st.session_state.sentence = ""
    st.session_state.results_shown = False
    st.rerun()

# Display the result if it exists
if st.session_state.results_shown and not generate_button:
    st.write("### Result:")
    st.success(st.session_state.sentence)