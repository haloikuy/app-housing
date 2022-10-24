import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Yuki')

df=pd.read_csv('housing.csv')
#add a slider
value_filter = st.slider('Median House Price', 0.0, 500001.0, 200000.0)

#add a location multi selcet
location_filter = st.sidebar.multiselect('Choose the location type',df.ocean_proximity.unique())

#add a radio button
income_filter = st.sidebar.radio('Choose income level',('Low','Medium','High'))

#filter by price

df = df[df.median_house_value <= value_filter]

#filter by location
df = df[df.ocean_proximity.isin(location_filter)]

#filter by income
if income_filter ==None:
    pass
elif income_filter =='Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income>2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income > 4.5]




#show on map
st.subheader('See more filters in the sidebar:')
st.map(df)

#show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(15, 10))
df.median_house_value.hist(bins=30,ax=ax)
st.pyplot(fig)




