import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Junior Writing Wizard", layout="wide")

# 1. Initialize All Systems
if 'stars' not in st.session_state:
    st.session_state.stars = 0
if 'stickers' not in st.session_state:
    st.session_state.stickers = []
if 'child_name' not in st.session_state:
    st.session_state.child_name = "Junior"
if 'custom_words' not in st.session_state:
    st.session_state.custom_words = "Lego, Atlanta, School, Family, Happy, Galaxy, Pizza"
if 'show_punchline' not in st.session_state:
    st.session_state.show_punchline = False

# 2. Lined Paper Styling (CSS)
st.markdown("""
    <style>
    .stCanvas {
        border: 3px solid #333 !important;
        background-color: white !important;
        background-image: 
            linear-gradient(0deg, transparent 95%, #7fafff 5%), /* Blue Top Line */
            linear-gradient(0deg, transparent 49%, #cccccc 50%, transparent 51%), /* Dashed Middle */
            linear-gradient(0deg, #ff7f7f 5%, transparent 5%); /* Red Bottom Line */
        background-size: 100% 300px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Databases
animal_stickers = ["🦁", "🐘", "🦒", "🐼", "🐙", "🐧", "🦖", "🦄", "🐝", "🦊"]
secret_jokes = [
    {"q": "What do you call a sleeping dinosaur?", "word": "SNORE", "a": "A Tyranno-snore-us! 🦖"},
    {"q": "What is a cat's favorite color?", "word": "PURPLE", "a": "Purr-ple! 🐈"},
    {"q": "Where do cows go on Saturday nights?", "word": "MOVIES", "a": "To the moo-vies! 🍿"},
    {"q": "What do you call a cold dog?", "word": "CHILI", "a": "A chili-dog! 🌭"}
]

if 'current_joke' not in st.session_state:
    st.session_state.current_joke = random.choice(secret_jokes)

# 4. Sidebar Navigation & Parent Settings
st.sidebar.title("🧙‍♂️ Writing Wizard")
st.sidebar.metric("Total Stars:", f"⭐ {st.session_state.stars}")

mode = st.sidebar.radio("Mission:", ["Lined Paper Tracing ✍️", "Secret Joke Mode 🤫", "Story Lab 📝", "Sticker Safari 🏆"])

st.sidebar.markdown("---")
with st.sidebar.expander("🔒 Parent Settings"):
    st.session_state.child_name = st.text_input("Wizard Name:", value=st.session_state.child_name)
    st.session_state.custom_words = st.text_area("Spelling Words (comma separated):", st.session_state.custom_words)

# 5. App Modes
if mode == "Lined Paper Tracing ✍️":
    st.title(f"✍️ {st.session_state.child_name}'s Tracing Lab")
    word_list = [w.strip() for w in st.session_state.custom_words.split(",")]
    target = st.selectbox("Pick a word to practice:", word_list)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"<h1 style='text-align: center; font-size: 80px; color: #E0E0E0; border: 2px dashed #DDD;'>{target}</h1>", unsafe_allow_html=True)
        st.write("Keep letters between the red and blue lines!")

    with col2:
        canvas_result = st_canvas(stroke_width=10, stroke_color="#2E86C1", background_color="rgba(0,0,0,0)", height=300, width=800, drawing_mode="freedraw", key=f"lined_{target}")

    if st.button("Check My Neat Writing! ✨"):
        st.session_state.stars += 2
        st.session_state.stickers.append(random.choice(animal_stickers))
        st.balloons()

elif mode == "Secret Joke Mode 🤫":
    st.title("🤫 The Secret Punchline")
    joke = st.session_state.current_joke
    st.subheader(f"Joke: {joke['q']}")
    st.write(f"Trace **'{joke['word']}'** to unlock the answer!")
    
    canvas_joke = st_canvas(stroke_width=10, stroke_color="#2E86C1", background_color="rgba(0,0,0,0)", height=250, width=600, drawing_mode="freedraw", key=f"joke_{joke['word']}")
    
    if st.button("Unlock Answer! 🔓"):
        st.session_state.show_punchline = True
        st.session_state.stars += 2
        st.balloons()

    if st.session_state.show_punchline:
        st.success(f"PUNCHLINE: {joke['a']}")
        if st.button("Next Joke ➡️"):
            st.session_state.current_joke = random.choice(secret_jokes)
            st.session_state.show_punchline = False
            st.rerun()

elif mode == "Story Lab 📝":
    st.title(f"📝 {st.session_state.child_name}'s Stories")
    story = st.text_area("Type your funny story here:", height=250)
    if st.button("Save Story 🌟"):
        st.session_state.stars += 5
        st.snow()

elif mode == "Sticker Safari 🏆":
    st.title(f"🦁 {st.session_state.child_name}'s Safari Collection")
    if st.session_state.stickers:
        cols = st.columns(6)
        for i, s in enumerate(st.session_state.stickers):
            cols[i % 6].markdown(f"<h1 style='text-align: center;'>{s}</h1>", unsafe_allow_html=True)
    else:
        st.write("Go trace some words to find animals for your safari!")
