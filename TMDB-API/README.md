# 🎬 Movie Recommendation System

A beautiful and interactive movie recommendation web application built with Streamlit and powered by The Movie Database (TMDb) API.

## ✨ Features

- **Interactive Movie Search**: Browse through your movie database with an intuitive sidebar search
- **Smart Recommendations**: Get personalized movie recommendations based on your selected movie
- **Rich Movie Details**: View movie posters, ratings, release dates, and overviews
- **Responsive Design**: Clean, modern UI with hover effects and smooth animations
- **Popular Movies**: Discover trending movies with curated default selections

## 🚀 Demo

The app provides two main interfaces:
- **Home Screen**: Features popular movies and search functionality
- **Recommendations Screen**: Shows detailed movie information and similar movie suggestions

## 📋 Prerequisites

Before running the application, ensure you have:

- Python 3.7 or higher
- A TMDb API key (free registration required)
- Movie dataset CSV file with movie names

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd movie-recommender
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas requests
   ```

3. **Set up your TMDb API**
   - Sign up at [The Movie Database](https://www.themoviedb.org/)
   - Get your API key from your account settings
   - Replace the Authorization token in the `HEADERS` section

4. **Prepare your dataset**
   - Create an `imdb_movies.csv` file with a `names` column containing movie titles
   - Place it in the same directory as the script

## 🎯 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Navigate the interface**
   - Use the sidebar to search for movies from your dataset
   - Click on popular movies from the home screen
   - Explore recommendations for any selected movie
   - View detailed movie information in the sidebar

## 🗂️ File Structure

```
movie-recommender/
│
├── app.py                 # Main Streamlit application
├── imdb_movies.csv        # Your movie dataset (required)
├── README.md              # This file
└── requirements.txt       # Python dependencies (optional)
```

## 🎨 Features Overview

### Movie Search
- Dropdown search with all movies from your dataset
- Dynamic movie selection with session state management

### Recommendations Engine
- Powered by TMDb's recommendation algorithm
- Displays up to 15 similar movies in a grid layout
- Shows movie posters, ratings, and titles

### User Interface
- Clean, professional design with blue accent color
- Responsive movie cards with hover effects
- Pill-shaped headers and smooth animations
- Mobile-friendly responsive layout

## 🔧 Configuration

### API Configuration
Update the `HEADERS` section in `app.py`:
```python
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer YOUR_TMDB_API_TOKEN_HERE"
}
```

### Dataset Format
Your `imdb_movies.csv` should have at least:
```csv
names
The Shawshank Redemption
The Godfather
The Dark Knight
...
```

## 🌟 Customization

### Adding More Default Movies
Edit the `default_movies` list in the main screen section:
```python
default_movies = [
    {"title": "Your Movie", "poster": "/poster_path.jpg"},
    # Add more movies...
]
```

### Styling
The CSS can be modified in the `st.markdown()` section to change:
- Color scheme (modify `--brand` variable)
- Layout dimensions
- Animation effects
- Card designs

## 🐛 Troubleshooting

### Common Issues

**Movie not found**: Ensure the movie name in your CSV matches TMDb's database
**API errors**: Check your TMDb API key and internet connection
**CSV errors**: Verify your CSV has a `names` column with proper formatting

### Error Handling
The app includes basic error handling for:
- Missing movie data
- API connection issues
- Invalid movie selections

## 📊 Performance

- Uses Streamlit's `@st.cache_data` for efficient data loading
- Optimized image loading with TMDb's CDN
- Session state management for smooth navigation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [The Movie Database (TMDb)](https://www.themoviedb.org/) for the comprehensive movie API
- [Streamlit](https://streamlit.io/) for the excellent web app framework
- Movie poster images courtesy of TMDb

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review TMDb API documentation
3. Open an issue in the repository

---

**Enjoy discovering your next favorite movie! 🍿**
