# 🎬 Movie Recommendation System - TF-IDF + KNN Approach

A machine learning-powered movie recommendation system that uses **TF-IDF vectorization** and **K-Nearest Neighbors (KNN)** algorithm to find similar movies based on plot descriptions and metadata.

## 📋 Overview

This implementation leverages traditional NLP techniques to create movie embeddings from plot overviews and uses KNN to find the most similar movies. The system combines the power of TF-IDF for feature extraction with KNN for similarity matching, providing accurate and interpretable recommendations.

## ✨ Features

- **AI-Powered Recommendations**: Uses TF-IDF + KNN machine learning model
- **Interactive Web Interface**: Beautiful Streamlit-based UI with modern design
- **Movie Posters & Info**: Integration with TMDB API for rich movie data
- **Real-time Search**: Fast movie search with autocomplete
- **Responsive Design**: Mobile-friendly interface with hover effects
- **15 Movie Recommendations**: Displays recommendations in a clean 5×3 grid layout

## 🛠️ Technology Stack

- **Machine Learning**: TF-IDF Vectorizer + K-Nearest Neighbors
- **Web Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Joblib (Pickle)
- **API Integration**: TMDB API for movie posters and metadata
- **Styling**: Custom CSS for modern UI design

## 📁 Project Structure

```
TFIDF-KNN/
├── pickle_model/
│   ├── knn_model.pkl           # Trained KNN model
│   ├── tfidf_vectorizer.pkl    # Fitted TF-IDF vectorizer
│   └── movies_metadata.csv     # Processed movie dataset
├── app.py                      # Main Streamlit application
├── model.ipynb                 # Model training notebook
├── imdb_movies.csv            # Raw movie dataset
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- TMDB API Key ([Get it here](https://www.themoviedb.org/settings/api))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd TFIDF-KNN
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up TMDB API Key**
   
   Edit `app.py` and replace `YOUR_TMDB_API_KEY` with your actual API key:
   ```python
   HEADERS = {
       "accept": "application/json",
       "Authorization": "Bearer YOUR_ACTUAL_API_KEY_HERE"
   }
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📊 How It Works

### 1. **Data Preprocessing**
- Movie plot overviews are cleaned and preprocessed
- TF-IDF vectorization converts text to numerical features
- Feature matrix captures important words and their relevance

### 2. **Model Training**
- KNN model is trained on TF-IDF vectors
- Cosine similarity is used as the distance metric
- Model finds k=16 nearest neighbors for recommendations

### 3. **Recommendation Process**
- User selects a movie from the interface
- System retrieves the movie's TF-IDF vector
- KNN finds 15 most similar movies based on plot similarity
- TMDB API enriches results with posters and metadata

## 🎯 Model Performance

- **Algorithm**: K-Nearest Neighbors with TF-IDF
- **Similarity Metric**: Cosine Similarity
- **Feature Engineering**: TF-IDF vectorization of movie overviews
- **Recommendation Quality**: High precision for plot-based similarity

## 🖥️ User Interface

- **Modern Design**: Clean, responsive interface with blue theme
- **Interactive Cards**: Hover effects and smooth animations
- **Smart Navigation**: Click any movie to get instant recommendations
- **Rich Information**: Movie posters, ratings, and release dates
- **Easy Search**: Sidebar search with all available movies

## 📈 Future Enhancements

- [ ] Add user rating-based filtering
- [ ] Implement collaborative filtering hybrid approach
- [ ] Add genre-based recommendations
- [ ] Include movie trailers and cast information
- [ ] Implement user preference learning

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- **TMDB** for providing the movie database API
- **IMDb** for the original movie dataset
- **Streamlit** for the amazing web framework
- **Scikit-learn** for machine learning tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) section
2. Create a new issue with detailed description
3. Include error messages and screenshots if applicable

---

**Built by Umar Faizan using TF-IDF + KNN Machine Learning**