import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY = 'AIzaSyDmVgtBtEqHyCPhEL4naok1ZjRdRmdB7iI'

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(role):
    """Translate user roles to display names."""
    if role == "model":
        return "Disaster Management Assistant"
    else:
        return role



def validate_user_input(input_text):
    """Validate user input to prevent empty or malicious inputs."""
    if not input_text.strip():
        st.error("Please enter a valid message.")
        return False
    return True


# Define a disaster management context
disaster_management_context = "As a Disaster Management Assistant, please assist with the following:\n\n"


st.set_page_config(
    page_title="DAI - Chatbot",
    page_icon=":brain:",  # Favicon emoji
    layout="wide")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Disaster AI - Chatbot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Disaster AI...")


if user_prompt and validate_user_input(user_prompt):
    # Prepend the disaster management context to the user's message
    full_prompt = disaster_management_context + user_prompt
    # Add user's message to chat and display it
    st.chat_message("user").markdown(full_prompt)

    # Send user's message to Disaster AI and get the response
    try:
        disaster_response = st.session_state.chat_session.send_message(full_prompt)
        # Display Disaster AI's response
        with st.chat_message("Disaster Management Assistant"):
            st.markdown(disaster_response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")