import streamlit as st
import pickle as pk
import pandas as pd

moviesList = pk.load(open('movies.pkl','rb'))

moviesListFinal = pd.DataFrame(moviesList)
similar = pk.load(open('similarity.pkl','rb'))

def recommend(movie):
    movieIndex = moviesListFinal[moviesListFinal['title']==movie].index[0]
    distances = similar[movieIndex]
    moviesList = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
    
    recommendedMovies=[]
    for i in moviesList:
        #add code to fetch movie posters from TMDB API
        recommendedMovies.append((moviesListFinal.iloc[i[0]].title))
    return recommendedMovies



st.title('Movie Recommender System')

selected = st.selectbox(
    'Search for a movie',
    moviesListFinal['title'].values)

if st.button('Recommend'):
    st.write('Recommended movies for you')
    selectedMovies = recommend(selected)
    for i in selectedMovies:
        st.write(i)



