import streamlit as st
import os
import openai
from openai import OpenAI

# Setting up the client with your API key. Make sure to set your API key in the environment variables.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def llm_response(user_review):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Classify the following review as having either a positive or negative sentiment."
            },
            {
                "role": "user",
                "content": user_review,
            }
        ],
    )
    return chat_completion.choices[0].message['content'].strip()

st.title("Review Sentiment Analyzer - Created by Razieh Akbari")

user_review = st.text_input("Please enter your review:")

if st.button("Analyze Sentiment"):
    if user_review:
        sentiment = llm_response(user_review)
        st.write(f"Review: {user_review}")
        st.write(f"Sentiment: {sentiment}")
    else:
        st.write("Please enter a review to analyze.")
