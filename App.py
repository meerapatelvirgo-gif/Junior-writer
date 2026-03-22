import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

# 1. Page Configuration
st.set_page_config(page_title="Junior Writing Wizard", layout="wide")

# 2. Force White Paper & Primary Lines (The Fix for Dark Mode)
st.markdown("""
    <style>
    /* Force the drawing area to be white paper */
    .stCanvas {
        border: 5px solid #FFD700 !important; /* Gold Wizard Border */
        background-color: white !important;
        background-image: 
            linear-gradient(0deg, transparent 95%, #7fafff 5%), /* Blue Top Line */
            linear-gradient(0deg, transparent 49%, #cccccc 50%, transparent 51%), /* Dashed Middle */
            linear-gradient(0deg, #ff7f7f 5%, transparent 5%); /* Red Bottom Line */
        background-size: 100% 300px;
        border-radius: 15px;
    }
    /* Make the rest of the text easy to read */
    .stApp { background-color: #0E1117; color: white; }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management (Stars & Stickers)
if 'stars' not in st.session_state:
    st.session_state.stars = 0
if 'stickers' not in st.session_state:
    st.session_state.stickers = []

# 4. Sidebar & Goals
st.sidebar.title("🧙‍♂️ Wizard Tools")
st.sidebar.metric("Total Stars:", f"⭐ {st.session_state.stars}")
st.sidebar.write(f"Stickers Found: {len(st.session_state.stickers)}")

# 5. The Tracing Lab
st.title("✍️ Junior's Tracing Lab")
word_list = ["Lego", "Atlanta", "School", "Family", "Happy", "Braves", "Pizza"]
target = st.selectbox("Pick a word to practice:", word_list)

col1, col2 = st.columns([1, 3])

with col1:
    # Visual Guide for letter height
    st.markdown(f"""
        <div style="height:300px; display:flex; align-items:center; justify-content:center; border:2px dashed #444; background:#1e1e1e; border-radius:10px;">
            <h1 style="font-size:80px; color
