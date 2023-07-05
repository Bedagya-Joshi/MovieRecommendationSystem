import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from functions import *
import random


def surprise():
    random_movie = random.choice(movies['title'].values)
    movie_index = new_df[new_df['title'] == random_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:2]

    suggested_movies = []
    suggested_genre = []
    suggested_director = []
    suggested_cast = []
    suggested_movie_posters = []

    for i in movies_list:
        movie_title = new_df.iloc[i[0]].title
        movie_poster = fetch_poster(new_df.iloc[i[0]].movie_id)
        movie_genre = movies.iloc[i[0]].genres[:3]
        movie_cast = movies.iloc[i[0]].cast[:5]
        movie_director = movies.iloc[i[0]].crew[:2]

        suggested_movies.append(movie_title)
        suggested_movie_posters.append(movie_poster)
        suggested_genre.append(", ".join(movie_genre))
        suggested_cast.append(", ".join(movie_cast))
        suggested_director.append(", ".join(movie_director))

    return suggested_movies, suggested_genre, suggested_director, suggested_cast, suggested_movie_posters


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_genre = []
    recommended_director = []
    recommended_cast = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_title = new_df.iloc[i[0]].title
        movie_poster = fetch_poster(new_df.iloc[i[0]].movie_id)
        movie_genre = movies.iloc[i[0]].genres[:3]
        movie_cast = movies.iloc[i[0]].cast[:5]
        movie_director = movies.iloc[i[0]].crew[:2]

        recommended_movies.append(movie_title)
        recommended_movies_posters.append(movie_poster)
        recommended_genre.append(", ".join(movie_genre))
        recommended_cast.append(", ".join(movie_cast))
        recommended_director.append(", ".join(movie_director))

    return recommended_movies, recommended_genre, recommended_director, recommended_cast, recommended_movies_posters


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')

movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

movies.dropna(inplace=True)

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert5)
movies['crew'] = movies['crew'].apply(fetch_dir)
movies.loc[:, 'overview'] = movies['overview'].apply(lambda x: x.split())
movies.loc[:, 'genre'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies.loc[:, 'keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies.loc[:, 'cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies.loc[:, 'crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['tags'] = movies['overview'] + movies['genre'] + movies['keywords'] + movies['cast'] + movies['crew']
new_df = movies[['movie_id', 'title', 'tags']]
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df.loc[:, 'tags'] = new_df['tags'].apply(stem)
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: x.lower())

# Apply TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = vectorizer.fit_transform(new_df['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_genre = []
    recommended_director = []
    recommended_cast = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_title = new_df.iloc[i[0]].title
        movie_poster = fetch_poster(new_df.iloc[i[0]].movie_id)
        movie_genre = movies.iloc[i[0]].genres[:3]
        movie_cast = movies.iloc[i[0]].cast[:5]
        movie_director = movies.iloc[i[0]].crew[:2]

        recommended_movies.append(movie_title)
        recommended_movies_posters.append(movie_poster)
        recommended_genre.append(", ".join(movie_genre))
        recommended_cast.append(", ".join(movie_cast))
        recommended_director.append(", ".join(movie_director))

    return recommended_movies, recommended_genre, recommended_director, recommended_cast, recommended_movies_posters


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')

movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

movies.dropna(inplace=True)

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert5)
movies['crew'] = movies['crew'].apply(fetch_dir)
movies.loc[:, 'overview'] = movies['overview'].apply(lambda x: x.split())
movies.loc[:, 'genre'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies.loc[:, 'keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies.loc[:, 'cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies.loc[:, 'crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['tags'] = movies['overview'] + movies['genre'] + movies['keywords'] + movies['cast'] + movies['crew']
new_df = movies[['movie_id', 'title', 'tags']]
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df.loc[:, 'tags'] = new_df['tags'].apply(stem)
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: x.lower())

# Apply TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = vectorizer.fit_transform(new_df['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)