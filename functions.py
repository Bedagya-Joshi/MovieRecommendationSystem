import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import requests
from PIL import Image
from io import BytesIO
import ast


ps = PorterStemmer()


def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l


def convert5(obj):
    l = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 5:
            l.append(i['name'])
            counter += 1
        else:
            break
    return l


def fetch_dir(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            l.append(i['name'])
            break
    return l


def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=86f1c812c2e391c40bad94515bce1d9e&language=en-US'.format(
            movie_id))
    data = response.json()
    if data['poster_path']:
        image_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Convert image format to JPEG
        if image.format != 'JPEG':
            image = image.convert('RGB')
            buffer = BytesIO()
            image.save(buffer, 'JPEG')
            buffer.seek(0)
            image = Image.open(buffer)

        return image
    else:
        return None