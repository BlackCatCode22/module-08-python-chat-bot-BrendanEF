# ChatBotApp.py
# Starter code for Python Chat Bot Program
# CIT-95 (Mohle) Spring 2024
# last updated: 4/24/24 by dH
# Suggested things to do:
#   Add chat memory
#   Use a local server like streamlit
#   Modify streamlit with HTML to make a nice looking chat bot
#   Use langchain framework to read .pdf files
#   Use an open source LLM that doesn't cost tokens


# pip install this dependency if you don't have this already
# pip install python-dotenv openai
# pip install --upgrade openai
# pip install --upgrade python-dotenv
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Configure the OpenAI library with your API key
openai.api_key = api_key

from openai import OpenAI
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

# User-defined function go here, before the main() function (is a Python coding convention)
def generate_response(user_input):
    try:

        messages = [
            {"role": "system",
             "content": "You are a wonderful assistant for comedians named Fozzie, and you help write jokes and funny stories."},
            {"role": "assistant", "content": "Hello fellow comedian! What is your name?"},
            {"role": "user", "content": "Hello. My name is Brendan."},
            {"role": "user", "content": "Tell me a joke."},
            {"role": "assistant", "content": "Why did the scarecrow win an award? Because he was outstanding in his field!"},
            {"role": "user", "content": "Tell me a funny story."},
            {"role": "assistant", "content": "One day, a man walked into a bar with a pet octopus. He sat down at the bar and ordered a beer for himself and a water for his octopus. The bartender, intrigued by the unusual pet, asked the man about the octopus."},
            {"role": "assistant", "content": "Why don't skeletons fight each other? They don't have the guts!"},
            {"role": "assistant", "content": "Why did the bicycle fall over? Because it was two tired!"},
            {"role": "user", "content": "What was your first joke?"},
            {"role": "user", "content": "What was your second joke?"},
            {"role": "user", "content": "What was your third joke?"},
            {"role": "user", "content": "What was your funny story about?"}
        ]  # The chatbot only seems to remember the content under the first "assistant" key/value pair. There is a limit to the total memory that the chatbot can store.

        # Call the OpenAI API to generate a response
        messages.append({"role": "user", "content": user_input})
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = messages)
        print(completion.choices[0].message)


        # Extract the text of the response
        response_text = completion['choices'][0]['message']['content']
        return response_text

    except Exception as e:
        # Print an error message if the API call fails
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."

def main():
    # This API key will not work (Because I deleted it after the video)
    # Use your own from OpenAI (there is a cost for this, but it is not much if you do not deploy
    # your app and have thousands of users) Typically, your API key will be in another Python file that
    # GitHub will not fork when asked to download
    # https://platform.openai.com/api-keys

    # Print a welcome message
    print("\nWelcome to the Standup Comedy Bot! Type 'quit' to exit.\n")

    # This loop will run until the break after user input "quit"
    while True:
        # Get user input.
        user_input = input("Talentless Comedian question: ")

        # Check if user wants to quit the chatbot
        if user_input.lower() == "quit":
            print("Exiting Standup Comedy Bot.")
            break

        # Generate a response using OpenAI's GPT-3.5-turbo
        response = generate_response(user_input)

        # Print the response
        print("Standup Comedy Bot:", response)

# Use this common Python idiom to check if your Python code is being run directly or being imported
# as a module into another program. This tells your program to start in a function named "main()"
# main() is not a reserved word in Python, but it is a standard convention and I suggest you use it
# to not confuse your project coworkers.
if __name__ == "__main__":
    main()
