import openai
import streamlit as st
import pandas as pd

st.header('Terminology to Thai')

# Set up the sidebar
st.sidebar.header('API Key')
api_key = st.sidebar.text_input('Enter your API key')

# Set up the main content
st.header('Terminology to Thai')

# Create a text box for the client to submit the paragraph
paragraph = st.text_area('Enter the paragraph')

# Add a submit button
if st.button('Submit'):
    # Process the paragraph using the API key
    if paragraph:
        # Summarize the text
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=paragraph,
            max_tokens=100,
            temperature=0.5,
            n=1,
            stop=None,
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

