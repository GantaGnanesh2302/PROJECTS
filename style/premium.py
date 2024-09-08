import streamlit as st
from PIL import Image

def app():
    image_path = "C:/Users/GNANESH GANTA/style/price.jpg"
    image = Image.open(image_path)
    st.image(image, caption='Your Image Caption', use_column_width=True)
if __name__ == "__main__":
    main()
