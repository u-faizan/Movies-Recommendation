import streamlit as st
import pandas as pd
import requests
import joblib

# --- LOAD DATA & MODEL ---
@st.cache_resource
def load_model():
    knn = joblib.load("pickle_model/knn_model.pkl")
    tfidf = joblib.load("pickle_model/tfidf_vectorizer.pkl")
    movies = pd.read_csv("pickle_model/movies_metadata.csv")
    return knn, tfidf, movies

knn, tfidf, movies_df = load_model()

# --- TMDB API Setup ---
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"

HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZWEyMTcyNTUzYWFkM2EwYTA3NjVmNGQ3NDYxYjE2MSIsIm5iZiI6MTc1Nzc1NjkxMS40MDIsInN1YiI6IjY4YzUzZGVmNzAyMWE5YjdiMGE4NjA1MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PuB2tOFuSgHF1oab9Ac7sE1FnVxsTsWMslIOw8zZum0"  # replace with your key
}

def search_movie_tmdb(query):
    url = f"{BASE_URL}/search/movie?query={query}"
    response = requests.get(url, headers=HEADERS).json()
    return response.get("results", [])

# --- RECOMMENDATION FUNCTION ---
def recommend(movie_title):
    if movie_title not in movies_df["names"].values:
        return []
    idx = movies_df[movies_df["names"] == movie_title].index[0]
    _, indices = knn.kneighbors(tfidf.transform([movies_df.iloc[idx]["overview"]]), n_neighbors=16)  # Get 16 to show 15 (excluding self)
    recs = []
    for i in indices.flatten()[1:]:  # skip self
        recs.append(movies_df.iloc[i]["names"])
    return recs

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# --- THEME / CSS ---
st.markdown("""
<style>
:root { --brand: #1e40af; }

.block-container {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    box-sizing: border-box;
}

.sidebar .sidebar-content { background-color: var(--brand); }
.sidebar .sidebar-content, .sidebar .sidebar-content * { color: #ffffff !important; }

.hero{
    background-color: var(--brand);
    color: #ffffff;
    display:flex;
    justify-content:center;
    align-items:center;
    margin: 28px auto 18px;
    padding: 18px 26px;
    min-height:76px;
    border-radius: 40px;
    box-shadow:0 10px 30px rgba(30,64,175,0.12);
    text-align:center;
    width: min(620px, 80%);
    box-sizing: border-box;
}
.hero h1 { margin:0; font-size:20px; }
.hero p { margin:6px 0 0 0; font-size:14px; color: #ffffff; }

.rec-header {
    background-color: var(--brand);
    color: #ffffff;
    display:flex;
    justify-content:center;
    align-items:center;
    margin: 20px auto;
    padding: 14px 26px;
    min-height:64px;
    border-radius: 36px;
    box-shadow: 0 10px 30px rgba(30,64,175,0.12);
    text-align:center;
    width: min(620px, 80%);
    box-sizing: border-box;
}
.rec-header h2 { margin:0; font-size:18px; font-weight:600; color:#ffffff; }

.movie-card{
    text-align:center;
    padding:10px;
    border-radius:12px;
    background-color:#ffffff;
    transition: transform 0.18s ease-in-out;
    margin-bottom:15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}
.movie-card:hover { transform: scale(1.06); }

.movie-card .stButton>button{
    background-color: var(--brand) !important;
    color: #ffffff !important;
    font-weight:600;
    width:100%;
    border-radius:8px;
    padding:7px 0;
    transition: transform 0.12s;
    border: none !important;
    white-space: normal;
}
.movie-card .stButton>button:hover{ transform: scale(1.03); }

.movie-rating {
    font-size: 14px;
    color: #666;
    margin: 8px 0;
    font-weight: 500;
}

.stButton>button { border-radius:8px; padding:6px 8px; }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "active_movie" not in st.session_state:
    st.session_state.active_movie = ""

# --- SIDEBAR SEARCH ---
st.sidebar.header("🎥 Movie Search")
st.sidebar.info("👉 Use the sidebar or click a movie to explore AI-powered recommendations.")
all_movie_names = movies_df["names"].dropna().unique().tolist()

sidebar_options = [""] + all_movie_names
current_active = st.session_state.active_movie
if current_active and current_active not in all_movie_names:
    sidebar_options.append(current_active)
try:
    sidebar_index = sidebar_options.index(current_active) if current_active else 0
except ValueError:
    sidebar_index = 0

sidebar_selection = st.sidebar.selectbox("Search a movie:", options=sidebar_options, index=sidebar_index)
if sidebar_selection != st.session_state.active_movie:
    st.session_state.active_movie = sidebar_selection
active_movie_name = st.session_state.active_movie

# --- MAIN SCREEN ---
if not active_movie_name:
    st.markdown(
        "<div class='hero'><div><h1>🎬 Movie Recommendation System</h1>"
        "<p>Discover movies similar to your favorites using AI! Search on the left to get started.</p></div></div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.subheader("🔥 Popular Movies")

    # Show some popular movies from your dataset as default options
    popular_movies_sample = movies_df["names"].dropna().head(10).tolist()
    
    # Display in rows of 5
    for row_start in range(0, min(len(popular_movies_sample), 10), 5):
        cols = st.columns(5)
        for i, movie_title in enumerate(popular_movies_sample[row_start:row_start+5]):
            with cols[i]:
                st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                
                # Try to get poster from TMDB
                search_results = search_movie_tmdb(movie_title)
                if search_results and search_results[0].get("poster_path"):
                    st.image(IMAGE_URL + search_results[0]["poster_path"], use_container_width=True)
                else:
                    st.markdown(
                        "<div style='height:300px; background: linear-gradient(135deg,#ddd,#f8f8f8); "
                        "display:flex; align-items:center; justify-content:center; border-radius:8px; color:#666;'>"
                        "🎬 No Image</div>",
                        unsafe_allow_html=True,
                    )
                
                if st.button(movie_title, key=f"popular_{row_start + i}"):
                    st.session_state.active_movie = movie_title
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
else:
    # Show sidebar poster & info
    search_results = search_movie_tmdb(active_movie_name)
    if search_results:
        selected_movie = search_results[0]
        poster_path = selected_movie.get("poster_path")
        if poster_path:
            st.sidebar.image(IMAGE_URL + poster_path, caption=active_movie_name, use_container_width=True)
        st.sidebar.markdown(f"**Release Date:** {selected_movie.get('release_date','N/A')}")
        st.sidebar.markdown(f"**Rating:** {selected_movie.get('vote_average','N/A')}/10")
        if selected_movie.get("overview"):
            st.sidebar.markdown(f"**Overview:** {selected_movie['overview'][:200]}...")

    if st.sidebar.button("🔄 Clear Selection"):
        st.session_state.active_movie = ""
        st.rerun()

    st.markdown(f"<div class='rec-header'><h2>🎞️ AI Recommendations for {active_movie_name}</h2></div>", unsafe_allow_html=True)
    st.markdown("---")

    # Get recommendations from your ML model
    recs = recommend(active_movie_name)
    if recs:
        # Show up to 15 recommendations in 3 rows of 5
        for row_start in range(0, min(len(recs), 15), 5):
            cols = st.columns(5)
            for i, rec_title in enumerate(recs[row_start:row_start+5]):
                with cols[i]:
                    st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                    
                    # Get poster and info from TMDB
                    rec_results = search_movie_tmdb(rec_title)
                    if rec_results:
                        rec_movie = rec_results[0]
                        poster_path = rec_movie.get("poster_path")
                        if poster_path:
                            st.image(IMAGE_URL + poster_path, use_container_width=True)
                        else:
                            st.markdown(
                                "<div style='height:300px; background: linear-gradient(135deg,#ddd,#f8f8f8); "
                                "display:flex; align-items:center; justify-content:center; border-radius:8px; color:#666;'>"
                                "🎬 No Image</div>",
                                unsafe_allow_html=True,
                            )
                        st.markdown(f"<div class='movie-rating'>⭐ {rec_movie.get('vote_average','N/A')}/10</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(
                            "<div style='height:300px; background: linear-gradient(135deg,#ddd,#f8f8f8); "
                            "display:flex; align-items:center; justify-content:center; border-radius:8px; color:#666;'>"
                            "🎬 No Image</div>",
                            unsafe_allow_html=True,
                        )
                        st.markdown("<div class='movie-rating'>⭐ N/A</div>", unsafe_allow_html=True)
                    
                    if st.button(rec_title, key=f"rec_{active_movie_name}_{row_start + i}"):
                        st.session_state.active_movie = rec_title
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found for this movie.")
        st.info("This movie might not be in our training dataset. Try searching for a different movie using the sidebar.")