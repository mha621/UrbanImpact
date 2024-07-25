#implement the page 6 that we talked about in the chat for reading a pdf'''
# we are using fitz or PyMuPDF'''
#import PyMuPDF
import fitz
import streamlit as st
import os
import openai
from openai import OpenAI
from pathlib import Path

# HTML for custom styling
st.markdown("""
<style>
.main-header {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #004d40;  /* Dark teal color */
}
.sub-header {
    font-size: 26px;
    text-align: center;
    color: #00796b;  /* Lighter teal */
}
.body-text {
    font-size: 18px;
    text-align: center;
    color: #333333;  /* Dark gray for readability */
}
.notice-consent {
    font-size: 18px;
    text-align: center;
    color: #FF0000 /* Red for notice of consent */
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Stay Updated with the Latest News 🗞️</h1>", unsafe_allow_html=True)
st.sidebar.markdown("# Stay Updated with the Latest News")

st.write("")
st.markdown('<div class="body-text">Stay informed about urban development and civic engagement in San Jose with ease! \
            Browse our curated list of PDF articles covering a broad spectrum of topics—from city planning and infrastructure improvements to community initiatives and walkability enhancements. \
            Select the article you\'re interested in and choose from three options: receive a concise summary, explore key points, or access the full transcription. \
            Whatever your preference, our app ensures you\'re well-informed on the latest discussions, plans, and news shaping the city\'s future.</div>', unsafe_allow_html=True)

st.write("")

st.markdown('<div class="notice-consent">By using this feature, you are choosing to accept our terms.</div>', unsafe_allow_html=True)

st.write("")

# Define the custom CSS
custom_css = """
<style>
    .stButton>button {
        color: white;
        background-color: #84BABF;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# if st.checkbox('I agree to the terms and conditions'):
    # Display some content when the checkbox is checked
    # st.write('You have agreed to our terms and conditions. Please proceed to stay updated on your city\'s latest news.')

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def get_summary(text):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

def get_key_points(text):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and extract the key points."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

def get_action_items(text):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

def get_sentiment(transcription):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible. Please keep it to fewer than 5 sentences."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content
# Create a file uploader
# uploaded_file = st.file_uploader("Choose a PDF file related to the issue of limited walkability in San Jose that you want to analyze. You will receive a summary, key points, action items, and a sentiment analysis of this PDF.", type="pdf")

#if uploaded_file is not None:
    # st.title("Stay Updated with the Latest News")

# Get a list of all the PDF files in the "articles" folder
pdf_files = [f for f in os.listdir(r'pages/articles') if f.endswith('.pdf')]

st.write("")
st.write("")
st.write("")
st.markdown('<div class="notice-consent">Please select an article from the list below before choosing what you would like to see, otherwise there will be nothing to display.</div>', unsafe_allow_html=True)
st.write("")
st.write("")
# Let the user select a file
selected_file = st.selectbox('Select one of the following articles:', pdf_files, help = 'Select an article from the list to view its summary, key points, or full transcription.')

# Let the user select an option
options = ['Summary', 'Key Points', 'Full Transcription']
selected_option = st.selectbox('What would you like to see?', options, help = 'Select an option to view the summary, key points, or full transcription of the selected article.')

# Open the selected file
selected_file_path = os.path.join(r'pages/articles', selected_file)

# Open the selected file
with fitz.open(selected_file_path) as doc:
    text = ""
    for page in doc:
        text += page.get_text("text")

if selected_option == 'Summary':
    # Get a summary of the text
    summary = get_summary(text)
    st.write(summary)
elif selected_option == 'Key Points':
    # Get the key points of the text
    key_points = get_key_points(text)
    st.write(key_points)
else:
    # Display the full transcription of the article
    st.write(text)
    # Load the PDF
    pdf = fitz.open(selected_file_path)
    
    # Concatenate the text from all pages
    full_text = ""
    for i in range(len(pdf)):
        page = pdf.load_page(i)
        full_text += page.get_text("text")



