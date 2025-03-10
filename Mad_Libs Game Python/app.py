import streamlit as st

# App Configuration
st.set_page_config(page_icon="✨", page_title="Mad Libs Game")
st.header("📜 Welcome to Mad Libs Game!")
st.write("💪 Are you ready to create a hilarious story? Fill in the blanks below!")
st.toast("The Mad_Libs Game!")

# Input Section
with st.form("madlibs_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Your Name:", placeholder="e.g., Alex")
        profession = st.text_input("Your Profession:", placeholder="e.g., Astronaut")
        food = st.text_input("Favorite Food:", placeholder="e.g., Pizza")
    
    with col2:
        city = st.text_input("Your City:", placeholder="e.g., New York")
        animal = st.text_input("Favorite Animal:", placeholder="e.g., Panda")
        mood = st.selectbox("Your Mood:", ["Happy", "Excited", "Curious", "Surprised"])
    
    # Submit Button
    if st.form_submit_button("✨ Generate Story"):
        if all([name, profession, food, city, animal]):
            # Story with fields
            story = f"""
            One day, **{name}**, a passionate **{profession}** from **{city}**, decided to try something new for dinner.
            Instead of the usual fare, **{name}** ordered a delicious **{food}** at a local restaurant. As the savory flavors danced on their tongue,
            an unexpected visitor—a friendly **{animal}**—joined the fun. **{name}** felt **{mood.lower()}** and realized that sometimes,
            the best moments in life come with a side of adventure. 🎉
            """
            
            # Story with all fields filled displayed here
            st.balloons()
            st.subheader("🌟 Your Mad Libs Story:")
            st.write(story)
    import streamlit as st

# Sidebar Section
st.sidebar.header("📖 How to Play")

st.sidebar.subheader("Step 1: Fill in the Blanks")
st.sidebar.write("- Enter your **name**")
st.sidebar.write("- Choose a **profession**")
st.sidebar.write("- Pick your **favorite food**")
st.sidebar.write("- Name a **city**")
st.sidebar.write("- Select an **animal**")
st.sidebar.write("- Choose your **mood**")

st.sidebar.subheader("✨ Step 2: Generate Your Story")
st.sidebar.write("Click the **'Generate Story'** button to create your unique Mad Libs story!")

st.sidebar.subheader("🎉 Step 3: Share & Enjoy")
st.sidebar.write("Copy your story and share it with friends for a good laugh! 😂")

st.sidebar.divider()  # Creates a horizontal line

st.sidebar.subheader("💡 Tips:")
st.sidebar.write("- Be **creative** with your answers!")
st.sidebar.write("- Try **different combinations** for unique stories")
st.sidebar.write("- Have fun and **don’t overthink it!**")

# Add About Section
st.sidebar.markdown("---")
st.sidebar.header("ℹ️ About")
st.sidebar.write("This Mad Libs game was created using:")
st.sidebar.write("- Python 🐍")
st.sidebar.write("- Streamlit 🎈")
st.sidebar.write("- Lots of creativity 🎨")
st.sidebar.write("Made with ❤️ by **Mutahir Bin Athar**")