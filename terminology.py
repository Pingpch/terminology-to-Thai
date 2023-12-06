import openai
import streamlit as st
import pandas as pd



# Set up the sidebar
st.sidebar.header('API Key')
api_key = st.sidebar.text_input('Enter your API key')
user_api_key = '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'
with st.sidebar:
 "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
 "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"



# Set up the main content
st.header('Terminology to Thai')

# Create a text box for the client to submit the paragraph
paragraph = st.text_area('Enter the paragraph')

# Add a submit button
if st.button('Submit'):
    # Process the paragraph using the API key
    if paragraph:
        # Summarize the text
        #openai.api_key = api_key
        openai.api_key = user_api_key
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": paragraph},
    ],
)
        summary = response.choices[0].text.strip()

        # Extract specific vocabulary
        vocabulary = ["word1", "word2", "word3"]  # Replace with your vocabulary extraction logic

        # Create a DataFrame to show the information
        data = {
            'Vocabulary': vocabulary,
            'Meaning': ['Meaning 1', 'Meaning 2', 'Meaning 3'],
            'Translation': ['Translation 1', 'Translation 2', 'Translation 3']
        }
        df = pd.DataFrame(data)

        # Display the DataFrame
        st.dataframe(df)
    else:
        st.warning('Please enter a paragraph before submitting.')
    pass

