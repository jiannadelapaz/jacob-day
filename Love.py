import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import random
import base64

# Function to encode and set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_background("black bg.jpg")

st.markdown(
    """
    <h1 style="font-size: 70px; font-weight: bold; text-align: left; margin-left: -180px; color: white;">
        Happy Birthday 
        <span class="jacob-gradient">&lt; Jacob &gt;</span>
        !
    </h1>

    <style>
    .jacob-gradient {
        background: linear-gradient(270deg, #833AB4, #1DB6FD, #FCF645, #F77539);
        background-size: 600% 600%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 5s ease infinite;
        display: inline-block;
        padding: 0 10px;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 80%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a line to change the font size of the messages
font_size = "30px"  # ← You can change this to any size (e.g., "30px", "50px")

# Messages that will display and animate
messages = [
    "I learned how to code..",
    "Following your footsteps..",
    "I love you!",
]

if "message_index" not in st.session_state:
    st.session_state.message_index = 0
else:
    st.session_state.message_index = (st.session_state.message_index + 1) % len(messages)

placeholder = st.empty()

# Typing + erasing animation using custom HTML and CSS
for message in messages:
    typed = ""
    # Typing
    for char in message:
        typed += char
        placeholder.markdown(
            f"<p style='font-size:{font_size}; color:white; margin-left:-180px;'>{typed}</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.05)

    time.sleep(1.5)  # Pause before erasing

    # Erasing
    for i in range(len(message), -1, -1):
        placeholder.markdown(
            f"<p style='font-size:{font_size}; color:white; margin-left:-180px;'>{message[:i]}</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.02)
        
# second page now
st.markdown(
    """
    <div style="
        margin-top: 100px;
        padding: 40px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        width: 90%;
        margin-right: 300px;
    ">
        <h2 style="
            font-family: 'Arial', monospace;
            font-size: 20px;
            color: white;
            text-align: center;
            margin: 0;
        ">
        Are you surprised? I've been working on practicing my coding over the past month and decided to make a digital birthday card my first project. I can't believe you're 21! I'm so grateful to have been able to spend your past four birthdays with you, and I can't wait to keep doing so. You're the light of my life, I hope you enjoy your special day.
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)

# for the end
st.rerun()