# 🎬 Movie Recommender System

This is a simple content-based movie recommender system built using Python, Pandas, and Streamlit. It suggests similar movies based on selected titles using cosine similarity over movie metadata.

---

## 📌 Features

- Recommends movies based on content similarity
- Uses TMDB 5000 movies dataset
- Built with an interactive Streamlit UI
- No external API (posters not fetched to keep it simple)

---

## 🗂️ File Structure
Movie_Recommender_System/
├── app.py # Streamlit application
├── MovieRecommenderSystem.ipynb # Jupyter notebook (initial work)
├── movies.pkl # Preprocessed movie data using Count Vectorizer
├── similarity_matrix.pkl 
├── tmdb_5000_credits.csv # Dataset - movie credits
├── tmdb_5000_movies.csv # Dataset - movies
├── requirements.txt # Required Python packages
├── README.md # Project documentation

---

## ▶️ Running Locally

1. Clone the repo:

```bash
git clone https://github.com/amanjuneja420/movie-recommender-system.git
cd movie-recommender-system

2.Install dependencies:
pip install -r requirements.txt

3.Run Streamlit:
streamlit run app.py

DATASET used:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

