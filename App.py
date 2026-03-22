import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.set_page_config(page_title="Junior Writing Wizard", layout="wide")

# 1. Setup & Secret Jokes
if 'stars' not in st.session_state:
    st.session_state.stars = 0
if 'child_name' not in st.session_state:
    st.session_state.child_name = "Junior"
if 'show_punchline' not in st.session_state:
    st.session_state.show_punchline = False

secret_jokes = [
    {"q": "What do you call a sleeping dinosaur?", "word": "SNORE", "a": "A Tyranno-snore-us! 🦖"},
    {"q": "What is a cat's favorite color?", "word": "PURPLE", "a": "Purr-ple! 🐈"},
    {"q": "Where do cows go on Saturday nights?", "word": "MOVIES", "a": "To the moo-vies! 🍿"},
    {"q": "What do you call a cold dog?", "word": "CHILI", "a": "A chili-dog! 🌭"},
    {"q": "Why did the golfer bring two pairs of pants?", "word": "HOLE", "a": "In case he got a hole in one! ⛳"}
]

if 'current_joke' not in st.session_state:
    st.session_state.current_joke = random.choice(secret_jokes)

# 2. Sidebar
st.sidebar.title("🧙‍♂️ Writing Wizard")
st.sidebar.metric("Stars:", f"⭐ {st.session_state.stars}")
st.session_state.child_name = st.sidebar.text_input("Wizard Name:", value=st.session_state.child_name)

mode = st.sidebar.radio("Mission:", ["Secret Joke Mode 🤫", "Story Time 📝", "Sticker Book 🏆"])

# 3. Secret Joke Logic
if mode == "Secret Joke Mode 🤫":
    st.title(f"🤫 {st.session_state.child_name}'s Secret Message")
    
    joke = st.session_state.current_joke
    st.subheader(f"Question: {joke['q']}")
    st.write(f"**Trace the word '{joke['word']}' to see the answer!**")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"<h1 style='text-align: center; font-size: 80px; color: #E0E0E0;'>{joke['word']}</h1>", unsafe_allow_html=True)
    
    with col2:
        canvas_result = st_canvas(stroke_width=10, stroke_color="#2E86C1", background_color="#FFFFFF", height=250, width=600, drawing_mode="freedraw", key=f"secret_{joke['word']}")

    if st.button("Unlock Answer! 🔓"):
        st.session_state.show_punchline = True
        st.session_state.stars += 2

    if st.session_state.show_punchline:
        st.balloons()
        st.success(f"ANSWER: {joke['a']}")
        if st.button("Next Secret Joke ➡️"):
            st.session_state.current_joke = random.choice(secret_jokes)
            st.session_state.show_punchline = False
            st.rerun()

elif mode == "Story Time 📝":
    st.title("📝 Story Lab")
    st.text_area("Write a funny story here:", height=200)
    if st.button("Save & Earn 5 Stars"):
        st.session_state.stars += 5
        st.balloons()

elif mode == "Sticker Book 🏆":
    st.title("🏆 Achievement Hall")
    st.write(f"Keep going, {st.session_state.child_name}! You have {st.session_state.stars} stars!")
