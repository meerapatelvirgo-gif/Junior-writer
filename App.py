import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

# 1. Page Configuration
st.set_page_config(page_title="Junior Writing Wizard", layout="wide")

# 2. Force White Paper & Primary Lines (The Fix for Dark Mode)
st.markdown("""
    <style>
    .stCanvas {
        border: 5px solid #FFD700 !important;
        background-color: white !important;
        background-image: 
            linear-gradient(0deg, transparent 95%, #7fafff 5%), 
            linear-gradient(0deg, transparent 49%, #cccccc 50%, transparent 51%), 
            linear-gradient(0deg, #ff7f7f 5%, transparent 5%);
        background-size: 100% 300px;
        border-radius: 15px;
    }
    .stApp { background-color: #0E1117; color: white; }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management
if 'stars' not in st.session_state:
    st.session_state.stars = 0
if 'stickers' not in st.session_state:
    st.session_state.stickers = []

# 4. Sidebar
st.sidebar.title("🧙‍♂️ Wizard Tools")
st.sidebar.metric("Total Stars:", f"⭐ {st.session_state.stars}")

# 5. The Tracing Lab
st.title("✍️ Junior's Tracing Lab")
word_list = ["Lego", "Atlanta", "School", "Family", "Happy", "Braves", "Pizza"]
target = st.selectbox("Pick a word to practice:", word_list)

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(f"""
        <div style="height:300px; display:flex; align-items:center; justify-content:center; border:2px dashed #444; background:#1e1e1e; border-radius:10px;">
            <h1 style="font-size:80px; color:#555; font-family:monospace;">{target}</h1>
        </div>
    """, unsafe_allow_html=True)
    st.write("Keep letters between the red and blue lines!")

with col2:
    canvas_result = st_canvas(
        stroke_width=10,
        stroke_color="#2E86C1",
        background_color="rgba(0,0,0,0)",
        height=300,
        width=800,
        drawing_mode="freedraw",
        key=f"canvas_{target}",
    )

# 6. Rewards
if st.button("I Finished My Neat Writing! ✨"):
    st.session_state.stars += 2
    animals = ["🦁", "🐘", "🦒", "🐼", "🐙", "🐧", "🦖", "🦄"]
    new_sticker = random.choice(animals)
    st.session_state.stickers.append(new_sticker)
    st.balloons()
    st.success(f"Great job! You earned 2 stars and a {new_sticker} sticker!")

# 7. Safari Collection
if st.session_state.stickers:
    st.markdown("---")
    st.subheader("🦁 Your Safari Collection")
        sticker_display = " ".join(st.session_state.stickers)
    st.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{sticker_display}</h1>", unsafe_allow_html=True)
