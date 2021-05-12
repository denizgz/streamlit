# Import Package
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

# Import data
# df = pd.read_csv("C:/Users/deniz/OneDrive - HWR Berlin/2. sem/Big Data and Architectures/gapminderviz-master/gapminder_tidy.csv")
# Import data
# df = pd.read_csv(r'C:\Users\deniz\OneDrive\Dokumente\GitHub\streamlit\life_pop_gni.csv')


# Draw a title and some text to the app:
'''
# Gapminder
'''

@st.cache
def get_data():
    return pd.read_csv(r'C:\Users\deniz\OneDrive\Dokumente\GitHub\streamlit\life_pop_gni.csv')

'# Year'

df = get_data()

min_year = int(df['year'].min())
max_year = int(df['year'].max())

countries = df['country'].unique()

'## By year'
year = st.slider('year', min_year, max_year)
df[df['year'] == year]

'## By country'
country = st.selectbox('country', countries)
df[df['country'] == country]


c = alt.Chart(df).mark_circle().encode(x='GNI', y='life_ exp',  color='GNI', tooltip=['GNI', 'life_exp'])
st.write(c)