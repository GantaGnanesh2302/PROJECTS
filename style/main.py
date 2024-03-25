import streamlit as st

from streamlit_option_menu import option_menu


import home, test,editing,premium,feedback, about
st.set_page_config(
        page_title="STYLE TRANSFER",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='STYLE TRANSFER ',
                options=['Home','Account','Editing','Premium','Feedback','about'],
                icons=['house-fill','person-circle','magic','diamond','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            test.app()    
        if app == "Editing":
            editing.app()        
        if app == 'Premium':
            premium.app()
        if app == 'Feedback':
            feedback.app()
        if app == 'about':
            about.app()    
             
          
             
    run()            
         
