import streamlit as st
from algorithms import *


movies = pd.DataFrame(new_df)

st.set_page_config(layout='wide')
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you want to be recommended based on?', movies['title'].values)

surprise_button = st.button('Surprise Me')
recommend_button = st.button('Recommend')


if surprise_button:
    suggested_movies, suggested_genre, suggested_director, suggested_cast, suggested_movie_posters = surprise()
    st.write("Surprise! Here's a random movie recommendation:")
    st.text('Name: ' + suggested_movies[0])
    st.text('Genre: ' + suggested_genre[0])
    st.text('Director: ' + suggested_director[0])
    st.text('Cast: ' + suggested_cast[0])
    st.image(suggested_movie_posters[0])



if recommend_button:
    names, genre, director, cast, posters = recommend(selected_movie_name)
    col1, col2 = st.columns(2)
    with col1:
        st.text('Name: ' + names[0])
        st.text('Genre: ' + genre[0])
        st.text('Director: ' + director[0])
        st.text('Cast: ' + cast[0])
        st.image(posters[0])
    with col1:
        st.text('Name: ' + names[1])
        st.text('Genre: ' + genre[1])
        st.text('Director: ' + director[1])
        st.text('Cast: ' + cast[1])
        st.image(posters[1])
    with col1:
        st.text('Name: ' + names[2])
        st.text('Genre: ' + genre[2])
        st.text('Director: ' + director[2])
        st.text('Cast: ' + cast[2])
        st.image(posters[2])
    with col2:
        st.text('Name: ' + names[3])
        st.text('Genre: ' + genre[3])
        st.text('Director: ' + director[3])
        st.text('Cast: ' + cast[3])
        st.image(posters[3])
    with col2:
        st.text('Name: ' + names[4])
        st.text('Genre: ' + genre[4])
        st.text('Director: ' + director[4])
        st.text('Cast: ' + cast[4])
        st.image(posters[4])
    with col2:
        st.text('Name:' + names[5])
        st.text('Genre:' + genre[5])
        st.text('Director:' + director[5])
        st.text('Cast:' + cast[5])
        st.image(posters[5])
