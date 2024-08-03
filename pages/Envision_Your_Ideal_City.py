import os
import openai
import streamlit as st
from PIL import Image
import requests
from openai import OpenAI
from pathlib import Path

# HTML for custom styling
st.markdown("""
<style>
.main-header {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: #333333; 
    font-family: 'Tahoma', sans-serif;
}
.sub-header {
    font-size: 32px;
    text-align: center;
    color: #00796b;
    font-family: 'Tahoma', sans-serif;
}
.body-text {
    font-size: 24px;
    text-align: center;
    color: #333333;
    font-family: 'Tahoma', sans-serif;
}
.notice-consent {
    font-size: 24px;
    text-align: center;
    color: #FF0000; 
    font-family: 'Tahoma', sans-serif;
}
.body-2 {
    font-size: 24px;
    color: #00796b; 
    font-family: 'Tahoma', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Envision Your Ideal City 📷</div>', unsafe_allow_html=True)
st.sidebar.markdown("# Envision Your Ideal City")

st.write("")
st.markdown('<div class="body-text">Envision your dream city by selecting features from a menu or describing your vision, \
            and watch our app bring it to life.</div>', unsafe_allow_html=True)

st.write("")

st.markdown('<div class="notice-consent">By using this feature, you are choosing to accept our terms and conditions.</div>', unsafe_allow_html=True)

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
        font-size: 24px;
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
    # st.write('You have agreed to our terms and conditions. Please proceed to visualize your improvements to see your ideal city.')

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def download_image(filename, url):
    response = requests.get(url)
    if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
    else:
            print("Error downloading image from URL:", url)

def filename_from_input(prompt):
# Remove all non-alphanumeric characters from the prompt except spaces.
    alphanum = ""
    for character in prompt:
        if character.isalnum() or character == " ":
            alphanum += character
    # Split the alphanumeric prompt into words.
    # Take the first three words if there are more than three. Else, take all    of them.
    alphanumSplit = alphanum.split()
    if len(alphanumSplit) > 3:
        alphanumSplit = alphanumSplit[:3]
    # Join the words with underscores and return the result.
    return "images/" + " ".join(alphanumSplit)


# Create an image
# If model is not specified, the default is DALL-E-2.
def get_image(prompt, model="dall-e-3"):
    image = client.images.generate(
        prompt=prompt,
        model=model,
        n=1,
        size="1024x1024"
    )
    # Download the image

    filename = str(Path(__file__).resolve().parent)+ "/"+ filename_from_input(prompt) + ".png"
    download_image(filename, image.data[0].url)

    return image


#print(response)
st.write("*"*40)

# Create a dropdown menu

features = ['expanded and improved sidewalks', 'more bike lanes', 'more green spaces like parks, gardens, trees, and flowers', 'better lighting in streets to improve safety', 'pedestrian streets, plazas, and courtyards to prioritize pedestrians over vehicles']

st.markdown('<div class="body-2">Option 1: Select a feature from the drop-down menu.</div>', unsafe_allow_html=True)
st.write("")
st.write("If you cannot think of any ideas about what you would like in your ideal city, feel free to choose from the dropdown menu below!")

selected_feature = st.selectbox('Select a feature you would like to see more of in your city:', features, help = "Select a feature from the dropdown menu to generate an image of your ideal city.")

# Display the selected feature
# st.write(f"You selected: {selected_feature}")


with st.form(key = "chat1"):
    # Include the selected feature in the prompt
    prompt = f"In my ideal city, I would like to have {selected_feature.lower()}."
    # st.text_input('**What features would you like to see in your ideal city?**"', value=prompt)
    submitted = st.form_submit_button("Submit")
    if submitted:
        response = get_image(prompt)
        image = Image.open(str(Path(__file__).parent)+'/'+filename_from_input(prompt)+'.png')
        st.image(image, caption='New Image')


st.write("")
st.write("*"*40)

st.markdown('<div class="body-2">Option 2: Write your own prompt.</div>', unsafe_allow_html=True)
st.write("")
st.write("Otherwise, if you know what you have an idea of what you would like in your ideal city, please type it in the text box below!")
# st.write("When describing your ideal city, try to be as specific as possible. For example, you could say 'I would like a city with lots of green spaces, bike lanes, and pedestrian-friendly streets. I would also like to have a park with a lake and a playground.' The more specific you are, the better the AI will be able to generate an image that matches your description.")

with st.form(key = "chat2"):
    prompt = st.text_input('**In your ideal city, what are some key features you would like to have?\
                        For example, you could say "I would like to have a park with a lake and a playground.**"', help = '''Type in the features you would like to see in your ideal city.\
                            When describing your ideal city, try to be as specific as possible. \
                                For example, you could say 'I would like a city with lots of green spaces, bike lanes, and pedestrian-friendly streets. \
                                    I would also like to have a park with a lake and a playground.' \
                                        The more specific you are, the better the AI will be able to generate an image that matches your description.''')
    submitted = st.form_submit_button("Submit")
        
    if submitted:
        response = get_image(prompt)
        image = Image.open(str(Path(__file__).parent)+'/'+filename_from_input(prompt)+'.png')
        st.image(image, caption='New Image')