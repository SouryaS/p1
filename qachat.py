import os
import streamlit as st
import google.generativeai as genai

# Try to load from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()  # loading all the environment variables
except Exception as e:
    st.error(f"Error loading .env file: {e}")

# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Check if API key is available
if not api_key:
    st.error("""
    ⚠️ **No API key found!** 
    
    Please set up your API key using one of these methods:
    
    1. Run `python create_env.py` in your terminal
    2. Create a `.env` file with your GOOGLE_API_KEY
    
    See API_SECURITY.md for more details.
    """)
    st.stop()  # Stop execution if no API key

# Configure the API
genai.configure(api_key=api_key)

## function to load Gemini model and get responses
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[])
except Exception as e:
    st.error(f"Error initializing Gemini model: {e}")
    st.stop()

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"Error getting response from Gemini: {e}")
        return None

## initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    if response:
        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
        
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    



    

