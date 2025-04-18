import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure at least one character type is selected
    if not characters:
        return "Please select at least one character type."

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Generator")

# Password options
length = st.slider("Select password length", min_value=8, max_value=32, value=12)
use_uppercase = st.checkbox("Include uppercase letters")
use_numbers = st.checkbox("Include numbers")
use_special_chars = st.checkbox("Include special characters")

# Generate button
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    if password.startswith("Please select"):
        st.error(password)
    else:
        st.success("Here is your secure password:")
        st.code(password, language="text")
