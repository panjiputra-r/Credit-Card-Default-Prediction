# import library
import streamlit as st
import pandas as pd
import numpy as np 

# import visualization
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

def run():
    # Set Title
    st.title('CREDIT CARD DEFAULT PAYMENT VISUALIZATION')

    # memasukkan gambar
    st.image ('https://akcdn.detik.net.id/visual/2018/04/13/6d6226ff-54c4-4308-91ef-c9643e4d80ff_169.jpeg?w=715&q=90')

    # markdown
    st.markdown ('---')

    # load data
    st.markdown('<h3 style="text-align:center;">Dataframe</h3>', unsafe_allow_html=True)
    data = pd.read_csv('P1G5_Set_1_panji_putra.csv')

    # menampilkan dataframe
    st.dataframe(data)
    st.markdown ('---')

    # menampilkan EDA
    st.markdown('## Exploratory Data Analysis (EDA)')

    # Visualisasi Distribusi Data Pada Kolom "Age"
    st.markdown ('---')
    st.markdown('### Distribusi Data Pada Kolom "Age"')
    fig, ax = plt.subplots(figsize=(15, 6))
    sns.histplot(data['age'], ax=ax)
    ax.set_title('Distribution of Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Visualisasi Boxplot
    st.markdown ('---')
    st.markdown('### Distribusi Data Pada Kolom "Limit_Balance"')
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.boxplot(x=data['limit_balance'], ax=ax)
    ax.set_title('Boxplot Distribusi Data untuk Variabel limit_balance')
    ax.set_xlabel('Limit Balance')
    st.pyplot(fig)

    # Visualisasi PieChart
    st.markdown ('---')
    st.markdown('### Presentase Kolom Default_Payment')
    fig, ax1 = plt.subplots()
    data['default_payment_next_month'].value_counts().plot(kind='pie', autopct='%.2f%%', labels=['0 = No', '1 = Yes'], ax=ax1)
    ax1.set_title("Presentase Kolom Default Payment")
    st.pyplot(fig)

    # Visualisasi Barchart
    st.markdown ('---')
    st.markdown('### Hubungan default payment dan gender')
    correlation_gender = data.groupby(['sex', 'default_payment_next_month']).size().unstack()
    fig, ax = plt.subplots()
    correlation_gender.plot(kind='bar', stacked=True, ax=ax)
    plt.xlabel('1 = Male, 2 = Female')
    plt.ylabel('Count')
    plt.title('Korelasi antara gender dan default payment')
    st.pyplot(fig)

    # Visualisasi Barchart
    st.markdown ('---')
    st.markdown('### Hubungan antara Education dan Default Payment')
    correlation_data = data.groupby(['education_level', 'default_payment_next_month']).size().unstack()
    fig, ax = plt.subplots()
    correlation_data.plot(kind='bar', ax=ax)
    plt.xlabel('Education Level')
    plt.ylabel('Count')
    plt.title('Hubungan antara Education dan Default Payment')
    st.pyplot(fig)

if __name__ == "__main__":
    run()
    