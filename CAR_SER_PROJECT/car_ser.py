import numpy as np
import pickle
import streamlit as st
st.sidebar.title("CAR SERVICES")
st.sidebar.write("**_washing_**")
st.sidebar.subheader("**_SPARE PARTS_**")
st.sidebar.title("**OUR MODELS**")
car_name={'VOLVO': 20, 'VOLKSWAGEN': 19, 'TOYATA': 18, 'FORD': 5, 'BENZ': 1, 'BMW': 2, 'KIA': 7, 'AUDI': 0, 'RENAULT': 13, 'PEUGEOT': 12, 'SKODA': 16, 'SAAB': 15, 'NISSAN': 10, 'OPEL': 11, 'HYUNDAI': 6, 'CITROEN': 4, 'MAZDA': 8, 'CHEVROLET': 3, 'MITSUBISHI': 9, 'SUBARA': 17, 'ROLLS ROYCE': 14}
for i in car_name.keys():
    st.sidebar.subheader(i)
with open("model.pkl",'rb') as f:
    model=pickle.load(f)
def predict(CAR_NAME, SERVICE,SIDEMIRROR,FRONTLIGHTS,BACKLIGHTS,TYRESET,TYRE,TUBE,SEATCOVER,ENGINE,AIR,BRAKE):
    #"""Function to accept data"""
    selected_car=car_name[CAR_NAME]
    input_data=np.array([[selected_car, SERVICE,SIDEMIRROR,FRONTLIGHTS,BACKLIGHTS,TYRESET,TYRE,TUBE,SEATCOVER,ENGINE,AIR,BRAKE]])
    return model.predict(input_data)[0]
if __name__=="__main__":
    st.header("WELCOME TO CAR GARAGE SERVICE")
    col1,col2=st.columns([2,1])
    CAR_NAME=col1.selectbox("select a car model",list(car_name.keys()))
    SERVICE=col1.number_input("washing",max_value=1,min_value=0,value=1,step=1)
    SIDEMIRROR=col1.number_input("SIDE MIRRORS",max_value=2,min_value=0,value=1,step=1)
    FRONTLIGHTS=col1.number_input("FRONT LIGHTS",max_value=2,min_value=0,value=1,step=1)
    BACKLIGHTS=col1.number_input("BACK LIGHTS",max_value=2,min_value=0,value=1,step=1)
    TYRESET=col2.slider("NO.OF.TYRES SETS",max_value=4,min_value=0,value=2)
    TYRE=col2.slider("NO.OF.TYRES",max_value=4,min_value=0,value=2)
    TUBE=col2.slider("NO.OF.TUBES",max_value=4,min_value=0,value=2)
    SEATCOVER=col2.slider("NO.OF.SEAT COVERS",max_value=4,min_value=0,value=2)
    ENGINE=col1.number_input("ENGINE REQUIRED",max_value=1,min_value=0,value=1,step=1)
    ENGINE_OIL=col1.number_input("KMS RAN FROM LAST SERVICE",max_value=5000,min_value=1000,value=5000,step=500)
    AIR=col2.slider("NO.OF.AC'S",max_value=4,min_value=0,value=2)
    BRAKE=col1.number_input("BRAKES REQUIRED",max_value=4,min_value=0,value=1,step=1)
    result=predict(CAR_NAME, SERVICE,SIDEMIRROR,FRONTLIGHTS,BACKLIGHTS,TYRESET,TYRE,TUBE,SEATCOVER,ENGINE,AIR,BRAKE)
    submit_button=st.button("Submit")
    if submit_button:
        if ENGINE_OIL<5000:
            st.write("**NO NEED TO REPLACE ENGINE OIL**")
        else:
            result+=5000
        larger_text=f"<h2 style='color:blue;'> THE ESTIMATION IS :₹{format(result,'.2f')}</h2>"
        st.markdown(larger_text,unsafe_allow_html=True)

