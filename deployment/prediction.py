# import library
import streamlit as st
import pandas as pd
import numpy as np 
import pickle

# load model yang sudah dibuat
with open("model.pkl", "rb") as model:
    model = pickle.load(model)

# function untuk menjalankan streamlit model predictor
def run():
    # Set Title
    st.title('CREDIT CARD PREDICTOR')

    # Sub Title
    st.subheader("This Page Will Focus On The Prediction Of Credit Card Default Payment")
    st.image('https://navi.com/blog/wp-content/uploads/2022/06/credit-card.jpg')

    # Buat Form Input data
    st.markdown('## Input Data')
    with st.form('my_form'):
        limit_balance = st.number_input('Limit Balance', min_value=0.0, max_value=999999999.00)
        education_level = st.selectbox('Education Level', options=[1, 2, 3, 4])
        pay_0 = st.selectbox('Repayment Status in September', options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_2 = st.selectbox('Repayment Status in August', options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_3 = st.selectbox('Repayment Status in July', options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_4 = st.selectbox('Repayment Status in June', options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_5 = st.selectbox('Repayment Status in May', options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        pay_6 = st.selectbox('Repayment Status in April', options=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

        submitted = st.form_submit_button('Lets Check!')

    # dataframe
    data = {
       'limit_balance' : limit_balance,
       'education_level' : education_level,
        'pay_0' : pay_0,
        'pay_2' : pay_2,
        'pay_3' : pay_3,
        'pay_4' : pay_4,
        'pay_5' : pay_5,
        'pay_6' : pay_6,
        }

    df = pd.DataFrame([data])
    st.dataframe(df)
    
    if submitted:
        pred_inf = model.predict(df)

        if pred_inf[0] == 0:
            st.write('Not Default')
        else:
            st.write('Default')

if __name__== '__main__':
    run()

