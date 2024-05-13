import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Configure the OpenAI library with your API key
openai.api_key = api_key

from openai import OpenAI
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

def main():
    # Initialize Streamlit application
    # streamlit run filepath
    st.set_page_config(page_title="Standup Comedy Chatbot", page_icon="🤖", layout="wide")

    # ----HEADER SECTION----
    with st.container():
        st.header("Python Chatbot using Streamlit and OpenAI ChatGPT 3.5")
        st.title("Standup Comedy Assistant")
        st.divider()

    # ----MAIN SECTION----
    with st.container():
        user_input = st.text_input("Ask me anything about Comedy", "")
        st.divider()
        # Tried to code st.form_submit_button to "clear on submit" in order to clear the st.text_input, but it remains in the True state which is preventing the output from working. I also tried a "Reset" st.button to clear the st.text_input, but it is also causing issues with the output. I removed the reset button code to avoid issues in the app.

    # ----OUTPUT SECTION----
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
                with st.chat_message("user"):
                    st.write("😆 :green[_Your question_:]", user_input)  # Display user input

        with right_column:
            with st.chat_message("assistant"):
                try:
                        if user_input:
                            completion = client.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system",
                                     "content": "You are a wonderful assistant for comedians named Fozzie, and you help write jokes and funny stories."},
                                    {"role": "user", "content": user_input}
                                ]
                            )

                            answer = completion.choices[0].message.content
                            st.write("🤖 :red[_Chatbot Response_:]", answer)

                except Exception as e:
                    st.write("🤖 :red[Chatbot Response:]", e)
                    return "I'm sorry, I couldn't generate a response."

if __name__ == "__main__":
    main()
