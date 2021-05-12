# Import Package
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

multiselect = st.sidebar.multiselect('Countries',pd.unique(df['country']))

subset = df.loc[(df.year==str(year)) & (df.country.isin(multiselect))]
st.write(subset)
fig, ax = plt.subplots()
ax.set(xscale="log")
ax.set_xlim([10**2, 10**5])

sns.scatterplot(data=subset, x="GNI", y="life_exp", size="pop", legend='brief',hue='country', sizes = (subset['pop'].min()/1000000, subset['pop'].max()/1000000))
st.pyplot(fig)

