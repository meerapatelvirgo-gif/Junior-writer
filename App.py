import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

# Page setup
st.set_page_config(page_title="Junior Writer Pro", layout="wide")
st.title("🚀 Junior Writer: Writing & Tracing Lab")

# 1. Database of 20 Advanced Prompts
prompts = [
    "If you had 100 LEGO bricks, what is the FIRST thing you would build?",
    "Imagine you shrunk to the size of an ant. What does the grass look like?",
    "Which is a better pet: a dog or a dragon? Give 3 reasons why.",
    "You found a secret door in the back of your closet. Where does it lead?",
    "Explain how to play your favorite game to someone who has never played it.",
    "If you were the Mayor of Atlanta for one day, what rule would you change?",
    "What do you think cars will look like in the year 2050?",
    "The power went out! Design a way to see in the dark without a flashlight.",
    "Describe what it feels like when it starts to rain on a hot summer day.",
    "What makes someone a good friend? Give an example.",
    "If animals could talk, which one would be the funniest?",
    "Design a new planet! What color is the sky and who lives there?",
    "Why is it important to learn math? Give a real-life example.",
    "What is the bravest thing you have ever done?",
    "If you could grow a tree that grew anything (not fruit), what would it grow?",
    "Write a 'Thank You' note to a teacher. What is the best thing they taught you?",
    "How do you make a perfect peanut-butter-free snack?",
    "If you were a superhero, what would your name and your 'logo' be?",
    "What is your favorite book? Write a review to convince a friend to read it.",
    "What is the best thing about being 7 years old?"
]

# 2. Sidebar Navigation
st.sidebar.title("Choose Activity")
choice = st.sidebar.radio("Go to:", ["📝 Story Writing", "✍️ Handwriting Lab"])

if choice == "📝 Story Writing":
    st.header("Today's Writing Challenge")
    
    if 'current_prompt' not in st.session_state:
        st.session_state.current_prompt = random.choice(prompts)
    
    if st.button("🔄 Give me a new idea!"):
        st.session_state.current_prompt = random.choice(prompts)
        
    st.info(f"**Prompt:** {st.session_state.current_prompt}")
    
    user_story = st.text_area("Type your story here:", height=300, placeholder="Once upon a time...")
    
    st.subheader("✅ Handwriting Checklist")
    c1, c2, c3 = st.columns(3)
    with c1: st.checkbox("Capital Letters")
    with c2: st.checkbox("Finger Spaces")
    with c3: st.checkbox("End Marks (. ! ?)")
    
    if st.button("Done! 🌟"):
        st.balloons()
        st.success("Story Saved! You earned 10 Star Points! ⭐")

elif choice == "✍️ Handwriting Lab":
    st.header("Neatness Practice")
    st.write("Use your finger or a stylus to trace your name or letters carefully on the lines!")
    
    # Simple Canvas for Tracing (Requires 'pip install streamlit-drawable-canvas')
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  
        stroke_width=3,
        stroke_color="#000000",
        background_color="#FFFFFF",
        # background_image= "URL_TO_LINED_PAPER_IMAGE" (Optional)
        height=400,
        drawing_mode="freedraw",
        key="canvas",
    )
    
    if st.button("Clear Canvas"):
        st.rerun()

