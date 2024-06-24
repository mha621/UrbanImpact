import streamlit as st
from openai import OpenAI
from PIL import Image
import openai
import os
import base64
import requests  

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

st.markdown("<h1 style='text-align: center;'>Analyze and Report Issues in Your City 📄</h1>", unsafe_allow_html=True)
st.sidebar.markdown("# Analyze and Report Issues in Your City")

st.write("")
st.markdown('<div class="body-text">Capture the essence of your city to identify and address urban challenges. \
        Share an image to highlight any issue—traffic problems, unsafe pedestrian areas, or anything that affects your daily life in San Jose. \
        Our AI-powered tool will analyze the image and provide insights to help us collectively enhance our urban environment. \
        Together, we can create a more vibrant, accessible, and engaging community.</div>', unsafe_allow_html=True)

st.write("")

st.markdown('<div class="notice-consent">By submitting an image, you agree to share it with our AI model for analysis. \
            The image will be used solely for the purpose of providing insights on urban issues and will not be stored or shared with third parties. \
            Click the button below to accept our terms and proceed to the image analysis and reporting feature.</div>', unsafe_allow_html=True)

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


if st.checkbox('I agree to the terms and conditions'):
    # Display some content when the checkbox is checked
    st.write('You have agreed to our terms and conditions. Please proceed to upload an image for analysis and reporting.')

    openai.api_key = os.environ["OPENAI_API_KEY"]

    client = OpenAI()

    # Your app code goes here
    # Function to encode the image
    def encode_image(image_path):
      with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
      
    st.write("*"*40)

    uploaded_file = st.file_uploader("**Submit an Image of an Issue in Your City Below:**", type=['jpg', 'png', 'jpeg'], help = "Drag and drop or browse to upload an image to analyze and report.")

    if uploaded_file is not None:      
      # Convert the file to an image
      uploaded_image = Image.open(uploaded_file)
      st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

      # Get the directory of the current script
      script_dir = os.path.dirname(__file__)

      # Save the image to the "images" folder
      image_path = os.path.join(script_dir, "images", uploaded_file.name)
      uploaded_image.save(image_path)

      # Getting the base64 string
      base64_image = encode_image(image_path)

      headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {openai.api_key}"
      }

      # Create a placeholder for the status message
      status_message = st.empty()
      status_message.write("Analyzing the image...")

      payload = {
      "model": "gpt-4-turbo",
        "messages": [
          {
          "role": "user",
          "content": [
              {
                "type": "text",
                "text": "What’s in this image? The answer to this first question should be titled in a larger font and bolded 'Analysis of the Image' followed by a new line\
                  How can it contribute to an undesirable experience in a city? The answer to this second question should be \
                    titled in a larger font and bolded 'Challenges Imposed' followed by a new line\
                      What can be done to improve these features in the photo to make a city more citizen-friendly?\
                        The answer to this third question should be titled in a larger font and bolded 'Suggestions for Improvement' followed by a new line"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": f"data:image/jpeg;base64,{base64_image}"
                }
              }
            ]
          }
        ],
        "max_tokens": 500
      }

      response = requests.post("https://api.openai.com/v1/chat/completions", headers = headers, json=payload)

      # Print the entire response
      chat_response = response.json()['choices'][0]['message']['content']

      # Split the chat response into lines
      lines = chat_response.split('  ')

      # Join the lines with newline characters
      chat_response = '\n'.join(lines)

      st.write(chat_response)

      # Create a button for reporting the issue
      if st.button('Report this issue'):
        # Write the chat response to the "results.txt" file
        with open('results.txt', 'a') as f:
          f.write(chat_response + '\n')
        st.write("Thank you for reporting the issue. Our team will review the feedback and take appropriate action. If it appears that the issue is severe enough, we will file a report to your local government to bring awareness to this issue.")
