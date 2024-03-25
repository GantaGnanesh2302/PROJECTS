import streamlit as st
def app():
    txt=st.text_area(
        label="YOUR FEEDBACK",height=300,max_chars=100,placeholder="write here"
        )
    st.write(txt)
    st.button("SUBMIT")
if __name__ == "__main__":
    main()

