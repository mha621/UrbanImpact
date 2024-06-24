import streamlit as st
from PIL import Image
import base64
import io
 

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
</style>
""", unsafe_allow_html=True)

# Display the custom-styled text
st.markdown('<div class="main-header">Welcome to Urban Impact!</div>', unsafe_allow_html=True)

# Open the image file
img = Image.open(r'pages/images/Urban_Impact_Logo_3.png')

# Resize the image
img = img.resize((300,275))

# Convert the image to a base64 string
buffered = io.BytesIO()
img.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Create three columns
col1, col2, col3 = st.columns([1,2,1])

# Display the image in the center column
with col2:
    st.image(img)

st.markdown('<div class="sub-header">Empowering Community Engagement in San Jose</div>', unsafe_allow_html=True)
st.markdown('<div class="body-text">Urban Impact goes beyond increasing walkability to enhance civic engagement throughout San Jose. With our innovative tools, you can report city issues, visualize solutions through image generation, and stay updated with the latest news in the city. Explore San Jose\'s streets through your lens, contribute to shaping its future, and engage with your community more deeply. Your insights drive the transformation towards a more vibrant and inclusive urban environment.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,2,2])

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

def feature_1():
    st.markdown('<div class="sub-header">Analyze and Report Issues in Your City</div>', unsafe_allow_html=True)
    st.image(r'pages/images/feat_1_ss.png')

def feature_2():
    st.markdown('<div class="sub-header">Envision Your Ideal City</div>', unsafe_allow_html=True)
    st.image(r'pages/images/feat_2_ss.png')

def feature_3():
    st.markdown('<div class="sub-header">Stay Updated with the Latest News</div>', unsafe_allow_html=True)
    st.image(r'pages/images/feat_3_ss.png')

with col1:
    if st.button("Analyze and Report Issues in Your City 📄"):
        feature_1()
with col2:
    if st.button("Envision Your Ideal City 🖼️"):
        feature_2()
with col3:
    if st.button("Stay Updated with the Latest News 🗞️"):
        feature_3()