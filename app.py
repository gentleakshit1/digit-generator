import streamlit as st
from model import generate_digit_images  # Assuming this function exists in model.py
from PIL import Image
import io

# --- Page config ---
st.set_page_config(
    page_title="Digit Converter for METI",
    layout="wide"
)

# --- Navbar ---
st.markdown(
    """
    <style>
        .navbar {
            background-color: #f63366;
            padding: 1rem;
            text-align: center;
            color: white;
            font-size: 24px;
            font-weight: bold;
            border-radius: 10px;
        }
    </style>
    <div class="navbar">Digit Converter for METI</div>
    """,
    unsafe_allow_html=True
)

st.write("## Select a Digit and Generate Images")

# --- Dropdown for digit selection ---
digit = st.selectbox("Choose a digit (0-9):", list(range(10)))

# --- Button to generate images ---
if st.button("Generate Images"):
    st.write(f"### Generated Images for Digit: {digit}")
    
    # Assuming generate_digit_images returns a list of 5 PIL.Image objects or byte data
    images = generate_digit_images(digit)  # Defined in model.py
    
    cols = st.columns(5)
    for col, img in zip(cols, images):
        # If byte data, convert to image
        if isinstance(img, bytes):
            img = Image.open(io.BytesIO(img))
        col.image(img, use_container_width=True)

# --- Footer ---
st.markdown(
    """
    <hr>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Developed by <b>Akshit Sharma</b> with ❤️ and ☕
    </div>
    """,
    unsafe_allow_html=True
)
