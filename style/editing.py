import streamlit as st
import os

def app():
    st.title("Style Transfer Project")

    # Upload content image
    content_image = st.file_uploader("upload content image", type=["jpg", "jpeg", "png"])
    style_images = st.file_uploader("Upload style image", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    # Upload style images
    st.write("\n\n")
    
    st.button("SUBMIT")
    if content_image is not None and style_images is not None:
        # Save content image to a temporary location
        content_temp_location = "temp_content_image.png"
        with open(content_temp_location, "wb") as f:
            f.write(content_image.read())

        st.image(content_temp_location, caption="Content Image", use_column_width=True)
        st.write("")

        # Save style images to temporary locations
        style_temp_locations = []
        for i, style_image in enumerate(style_images):
            style_temp_location = f"temp_style_image_{i}.png"
            with open(style_temp_location, "wb") as f:
                f.write(style_image.read())
            style_temp_locations.append(style_temp_location)

            # Display style images
            st.image(style_temp_location, caption=f"Style Image {i+1}", use_column_width=True)
            st.write("")
        import tensorflow_hub as hub
        import tensorflow as tf
        from matplotlib import pyplot as plt
        import numpy as np
        import cv2
        model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        def load_image(img_path):
            img = tf.io.read_file(img_path)
            img = tf.image.decode_image(img, channels=3)
            img = tf.image.convert_image_dtype(img, tf.float32)
            img = img[tf.newaxis, :]
            return img
        content_image = load_image(content_temp_location)
        style_image = load_image(style_temp_location)
        stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
        st.image(np.squeeze(stylized_image),width=600)

        st.write("Performing style transfer...")

        # You can perform style transfer using the content and style images here

        # Optional: Remove temporary files after processing
        os.remove(content_temp_location)
        for style_temp_location in style_temp_locations:
            os.remove(style_temp_location)
        

if __name__ == "__main__":
    main()
