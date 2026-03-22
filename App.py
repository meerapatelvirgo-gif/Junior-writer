import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.set_page_config(page_title="Junior Writing Wizard", layout="wide")

# 1. Setup
if 'stars' not in st.session_state:
    st.session_state.stars = 0
if 'child_name' not in st.session_state:
    st.session_state.child_name = "Junior"

# 2. THE SECRET SAUCE: Lined Paper Styling
# This adds the red and blue lines to the background of the tracing box
st.markdown("""
    <style>
    .stCanvas {
        border: 2px solid #333 !important;
        background-image: 
            linear-gradient(#f1f1f1 1px, transparent 1px), 
            linear-gradient(0deg, #ff7f7f 1px, transparent 1px), /* Red Bottom Line */
            linear-gradient(0deg, #7fafff 1px, transparent 1px); /* Blue Top Line */
        background-size: 100% 100px, 100% 250px, 100% 50px;
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
st.sidebar.title("🧙‍♂️ Writing Wizard")
st.sidebar.metric("Total Stars:", f"⭐ {st.session_state.stars}")
st.session_state.child_name = st.sidebar.text_input("Wizard Name:", value=st.session_state.child_name)

# 4. Tracing Lab
st.title(f"✍️ {st.session_state.child_name}'s Lined Paper Practice")
target_word = st.selectbox("Choose a word to trace:", ["Lego", "Atlanta", "School", "Family", "Happy"])

col1, col2 = st.columns([1, 3])
with col1:
    # This acts as the visual guide for letter height
    st.markdown(f"""
        <div style="height:300px; display:flex; align-items:center; justify-content:center; border:2px dashed #ccc; background:#f9f9f9;">
            <h1 style="font-size:80px; color:#D3D3D3; font-family:monospace;">{target_word}</h1>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # The Drawing Canvas
    canvas_result = st_canvas(
        stroke_width=10,
        stroke_color="#2E86C1",
        background_color="rgba(255, 255, 255, 0)", # Makes it see-through to show lines
        height=300,
        width=800,
        drawing_mode="freedraw",
        key="lined_canvas",
    )

if st.button("I Finished My Neat Writing! ✨"):
    st.session_state.stars += 2
    st.balloons()
    st.success("Great job keeping your letters on the lines!")
