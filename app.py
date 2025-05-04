import streamlit as st
import pickle
import pandas as pd
import numpy as np
import gdown
import os

file_id = "1RVsQo6_xgEb4o3KxMaH1QvPgOYHeRoa4"  # Replace with your actual ID
url = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"

output = "similarity_matrix.pkl"
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)



# Load and prepare movie list
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = pd.DataFrame(movies['title'].values, columns=['title'])
# movies_list['title'] = movies_list['title']

# Load similarity matrix
similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))

# Streamlit UI
st.title("Movie Recommender System")
st.write("This is a simple movie recommender system built with Streamlit.")
st.write("You can use this app to get movie recommendations based on your preferences.")

selected_movie_name = st.selectbox(
    'Select a movie genre',
    movies_list['title']
)

def recommend(movie_name):
    movie_index = movies_list[movies_list["title"] == movie_name].index[0]
    distance = similarity_matrix[movie_index]
    recommended_indices = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in recommended_indices:
        recommended_movies.append(movies_list.iloc[i[0]].title)

    return recommended_movies

if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie_name)
    st.write("You selected:", selected_movie_name)
    st.write("Based on your selection, we recommend the following movies:")
    for rec in recommendations:
        st.header(rec)
