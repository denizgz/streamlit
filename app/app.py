# Import Package
import streamlit as st
import pandas as pd
import plotly.express as px

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
df.GNI.fillna(0)

'## By year'
year = st.slider('year', min_year, max_year, step=1)
df[df['year'] == year]

'## By country'
country = st.selectbox('country', countries)
df[df['country'] == country]

# gdp_le = px.scatter(df, x="GNI", y="life_exp", text="country", log_x=True, size_max=60)
# st.title(f'GDP per capita and Life Expectancy in {country} in {year}')
# st.plotly_chart(gdp_le)


with st.echo(code_location='below'):
    import plotly.express as px

    fig = px.scatter(
        x=df["GNI"],
        y=df["life_exp"],
        log_x=True,
        hover_name=df['country'],
        size=df['pop'],
        range_x=[1,120000],
        range_y=[0,90]

    )
    fig.update_layout(
        xaxis_title="GNI",
        yaxis_title="Life expectation",
    )

    st.write(fig)