import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import plotly.express as px  # pip install plotly-express













# find more emoji :- https://www.webfx.com/tools/emoji-cheat-sheet/


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
         return none
    return r.json()
# ----------- -----------------


#==============Asset-------------


lottie_coding = load_lottieurl("https://lottie.host/9bcabe7c-c717-4b1f-8e48-8446f807e6af/2QPQR0e3Rg.json")

st.title("Tejas sahare")
st.sidebar.success("select a page above.")

with st.container():
    st.write("___")

col1 , col2 = st.columns(2 )
with col1:
 img = Image.open("123.png")
 st.image( img)


with col2:

    st.subheader("Hi, I am Tejas 👋")
    st.title('Data Analyst From India')

    st.write("I am Passionate about finding ways to use python be more efficient and effective in business setting.")
    st.write("[Learn More >](https://www.youtube.com/channel/UCpEsrYd-6i0fhpcbgAp9fJg)")

st.write("##")

with st.container():
    st.write("#")
    st.header("What I Do")

    st.write("""
               On my YouTube channel I am creating tutorials for people who:
               - are looking for a way to leverage the power of python in their day-to-day work.
               - are struggling with repetitive tasks in Excel and are looking for a way to use python 
               - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
               - are working With Excel and Themselves Thinking - "there has to be a better way. "

                If this sounds interesting to you consider subscribing and turning on the notification,.
         """)
    st.write("[YouTube Channel >](https://www.youtube.com/channel/UCpEsrYd-6i0fhpcbgAp9fJg)")


      #st_lottie(lottie_coding, height=350, key="analytics")

#--------------------------------------------------------------------------------------------
