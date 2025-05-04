import streamlit as st

st.title("Movie Recommender System")
st.write("This is a simple movie recommender system built with Streamlit.")
st.write("You can use this app to get movie recommendations based on your preferences.")

option = st.selectbox(
    'Select a movie genre',
    ('Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi')
)