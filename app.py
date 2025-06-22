import streamlit as st
from model import generate_digit_images
from PIL import Image
import io

st.set_page_config(page_title="Digit Converter", layout="wide")

# --- Enhanced Responsive Navbar ---
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f63366;
            padding: 1rem 2rem;
            border-radius: 10px;
            flex-wrap: wrap;
        }
        .navbar span {
            font-size: 24px;
            font-weight: 700;
            color: white;
        }
        .navbar-links {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        .navbar-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            font-size: 16px;
            position: relative;
            transition: transform 0.3s ease;
        }
        .navbar-links a::after {
            content: "";
            position: absolute;
            bottom: -3px;
            left: 0;
            width: 0%;
            height: 2px;
            background-color: white;
            transition: width 0.3s ease;
        }
        .navbar-links a:hover {
            transform: translateY(-2px);
        }
        .navbar-links a:hover::after {
            width: 100%;
        }
        @media (max-width: 600px) {
            .navbar {
                flex-direction: column;
                text-align: center;
                gap: 1rem;
            }
            .navbar-links {
                justify-content: center;
            }
        }
    </style>

    <div class="navbar">
        <span>Digit Converter</span>
        <div class="navbar-links">
            <a href="https://www.instagram.com/gentle.akshit/" target="_blank">Instagram</a>
            <a href="https://github.com/gentleakshit1" target="_blank">GitHub</a>
            <a href="https://www.youtube.com/@GentleAkshit" target="_blank">YouTube</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Main App ---
st.write("## Select a Digit and Generate Images")

digit = st.selectbox("Choose a digit (0–9):", list(range(10)))

if st.button("Generate Images"):
    st.write(f"### Generated Images for Digit: {digit}")
    images = generate_digit_images(digit)

    cols = st.columns(5)
    for col, img in zip(cols, images):
        if isinstance(img, bytes):
            img = Image.open(io.BytesIO(img))
        col.image(img, use_container_width=True)

# --- Footer ---
st.markdown("""
<hr>
<div style='text-align: center; color: gray; font-size: 14px;'>
    Developed by <b>Akshit Sharma</b> with ❤️
</div>
""", unsafe_allow_html=True)
