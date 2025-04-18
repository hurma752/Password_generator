import streamlit as st
import random
import string
import re

# Blocklist of common passwords
blacklist = ["password", "123456", "password123", "admin", "qwerty", "abc123"]

# Password Strength Checker function
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This password is too common. Choose something more secure.")
        return 1, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Password generator function
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += "!@#$%^&*"

    if not characters:
        return "Please select at least one character type."

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit App Interface
st.title("🔐 Password Strength Meter & Generator")

st.header("🔎 Check Your Password Strength")
user_password = st.text_input("Enter a password to check its strength:", type="password")

if user_password:
    score, feedback = check_password_strength(user_password)

    st.subheader("🧠 Feedback")
    for item in feedback:
        st.error(item)  # 👈 shows each item as an error

    st.subheader("🔒 Password Strength")
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
    else:
        st.error("❌ Weak Password - Please follow the suggestions above.")

st.markdown("---")

st.header("🔧 Generate a Strong Password")

# Password generator options
length = st.slider("Select password length", min_value=8, max_value=32, value=12)
use_uppercase = st.checkbox("Include uppercase letters", value=True)
use_numbers = st.checkbox("Include numbers", value=True)
use_special_chars = st.checkbox("Include special characters (!@#$%^&*)", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    if password.startswith("Please select"):
        st.error(password)
    else:
        st.success("Here is your secure password:")
        st.code(password)
