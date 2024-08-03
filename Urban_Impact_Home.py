import streamlit as st
from PIL import Image
import base64
import io
 

# HTML for custom styling
st.markdown("""
<style>
.main-header {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: #004d40;
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
</style>
""", unsafe_allow_html=True)

# Display the custom-styled text
st.markdown('<div class="main-header">Welcome to SJ Urban Impact!</div>', unsafe_allow_html=True)
st.write("")
st.write("")

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

st.write("")
#st.markdown('<div class="sub-header">Empowering Community Engagement in San Jose</div>', unsafe_allow_html=True)
st.markdown('<div class="body-text">Our goal at SJ Urban Impact is to enhance civic engagement by providing innovative tools for reporting\
            city issues, visualizing solutions, staying updated on local news, and contributing to a virbant urban environment.</div>', unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown('<div class="sub-header">Please feel free to click around and explore the 3 main features of this app using the sidebar on the left.</div>', unsafe_allow_html=True)
st.write("")

#st.markdown('<div class="body-text">Feature 1: Analyze and Report Issues in Your City</div>', unsafe_allow_html=True)
#st.markdown('<div class="body-text">Feature 2: Envision Your Ideal City</div>', unsafe_allow_html=True)
#st.markdown('<div class="body-text">Feature 3: Stay Updated with the Latest News</div>', unsafe_allow_html=True)
#col1, col2, col3 = st.columns([2,2,2])

# Define the custom CSS
#custom_css = """
#<style>
    #.stButton>button {
        #color: white;
        #background-color: #84BABF;
        #border: none;
        #padding: 15px 32px;
        #text-align: center;
        #text-decoration: none;
        #display: inline-block;
        #font-size: 16px;
        #margin: 4px 2px;
        #cursor: pointer;
        #border-radius: 4px;
    #}
#</style>
#"""

# Inject the custom CSS
#st.markdown(custom_css, unsafe_allow_html=True)

#def feature_1():
    #st.markdown('<div class="sub-header">Analyze and Report Issues in Your City</div>', unsafe_allow_html=True)
    #st.image(r'pages/images/feat_1_ss.png')

#def feature_2():
    #st.markdown('<div class="sub-header">Envision Your Ideal City</div>', unsafe_allow_html=True)
    #st.image(r'pages/images/feat_2_ss.png')

#def feature_3():
    #st.markdown('<div class="sub-header">Stay Updated with the Latest News</div>', unsafe_allow_html=True)
    #st.image(r'pages/images/feat_3_ss.png')

#with col1:
    #if st.button("Analyze and Report Issues in Your City 📄"):
        #feature_1()
#with col2:
    #if st.button("Envision Your Ideal City 🖼️"):
        #feature_2()
#with col3:
    #if st.button("Stay Updated with the Latest News 🗞️"):
        #feature_3()
