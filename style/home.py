import streamlit as st
from firebase_admin import firestore
from PIL import Image

def app():
    st.header(' :violet[WELCOME TO THE REALISTIC STYLE TRANSFER] ')
    image_path="C:/Users/GNANESH GANTA/style/sty.jpeg"
    img=Image.open(image_path)
    st.image(img,width=600)
    
    
    
    
    
