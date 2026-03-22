import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
st.set_page_config(page_title="Junior Wizard", layout="wide")
st.markdown("<style>.stCanvas { border: 5px solid #FFD700 !important; background-color: white !important; background-image: linear-gradient(0deg, transparent 95%, #7fafff 5%), linear-gradient(0deg, transparent 49%, #cccccc 50%, transparent 51%), linear-gradient(0deg, #ff7f7f 5%, transparent 5%); background-size: 100% 300px; } .stApp { background-color: #0E1117; color: white; }</style>", unsafe_allow_html=True)
if 'stars' not in st.session_state: st.session_state.stars = 0
if 'stickers' not in st.session_state: st.session_state.stickers = []
st.title("✍️ Junior's Tracing Lab")
target = st.selectbox("Word:", ["Lego", "Atlanta", "School", "Family", "Happy"])
st_canvas(stroke_width=10, stroke_color="#2E86C1", background_color="rgba(0,0,0,0)", height=300, width=800, drawing_mode="freedraw", key=f"c_{target}")
if st.button("I Finished! ✨"):
    st.session_state.stars += 2
    st.session_state.stickers.append(random.choice(["🦁", "🐘", "🦒", "🐼", "🐙", "🐧", "🦖", "🦄"]))
    st.balloons()
if st.session_state.stickers:
    st.write("---")
    st.markdown(f"<h1 style='text-align: center;'>{' '.join(st.session_state.stickers)}</h1>", unsafe_allow_html=True)
