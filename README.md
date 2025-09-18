# 🎬 Movies Recommendation System

A comprehensive exploration of movie recommendation algorithms, featuring **three distinct approaches** from traditional machine learning to cutting-edge AI. This repository demonstrates the evolution of recommendation systems, comparing different methodologies and their effectiveness.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movies-recommendation-using-sentence-transformer.streamlit.app/)

## 🎥 Demo

**🔴 Live Demo Video:** [Watch on GitHub](https://github.com/u-faizan/Movies-Recommendation)

**🚀 Interactive Demo:** [Try the App](https://movies-recommendation-using-sentence-transformer.streamlit.app/) *(Sentence Transformer implementation)*

## 📋 Project Overview

This repository contains three different movie recommendation systems, each showcasing a unique approach to understanding and suggesting similar movies. From API-based recommendations to deep semantic analysis, explore how different technologies solve the same problem.

```
Movies-Recommendation/
│
├── 🌐 TMDB-API/              # API-based recommendations
├── 🧮 TFIDF-KNN/             # Traditional ML approach  
├── 🧠 Sentence-Transformer/   # Deep learning semantic analysis
└── 📖 README.md              # This overview
```

## 🚀 Three Approaches Explained

### 1. 🌐 **TMDB-API Approach**
> **"Pure API-Powered Recommendations"**

**What it is:** Leverages The Movie Database (TMDB) API's built-in recommendation engine.

**How it works:**
- Fetches recommendations directly from TMDB's curated database
- Uses collaborative filtering and popularity metrics
- Real-time data with the latest movies and ratings

**Strengths:**
- ✅ Always up-to-date with new releases
- ✅ No local model training required  
- ✅ Leverages crowd-sourced data from millions of users
- ✅ Fast and reliable

**Best for:** Quick prototypes, always-current recommendations, production systems with API budget

---

### 2. 🧮 **TF-IDF + KNN Approach**  
> **"Classic Machine Learning"**

**What it is:** Traditional NLP using Term Frequency-Inverse Document Frequency with K-Nearest Neighbors.

**How it works:**
- Converts movie plot descriptions into TF-IDF vectors
- Uses cosine similarity to find nearest neighbors
- Trained on local dataset for consistent results

**Strengths:**
- ✅ Interpretable and explainable results
- ✅ Fast inference once trained
- ✅ Works offline without external APIs
- ✅ Solid baseline for text-based recommendations

**Best for:** Understanding recommendation fundamentals, educational purposes, lightweight deployment

---

### 3. 🧠 **Sentence Transformers Approach** ⭐
> **"State-of-the-Art Semantic AI"**

**What it is:** Deep learning using pre-trained transformer models for semantic understanding.

**How it works:**
- Creates dense vector embeddings using BERT-based models
- Captures semantic meaning, context, and nuanced relationships
- Uses cosine similarity on high-dimensional embeddings

**Strengths:**
- ✅ **Superior semantic understanding** - understands context and synonyms
- ✅ **Handles complex plots** - captures nuanced storylines and themes  
- ✅ **Cultural awareness** - recognizes genre and cultural patterns
- ✅ **Future-proof** - leverages cutting-edge NLP research

**Best for:** Production systems requiring highest accuracy, research projects, showcasing AI capabilities

## 📊 Comparison Matrix

| Feature | TMDB-API | TF-IDF + KNN | Sentence Transformers |
|---------|----------|--------------|----------------------|
| **Accuracy** | High (crowd-sourced) | Medium | **Highest** |
| **Semantic Understanding** | Basic | Limited | **Advanced** |
| **Setup Complexity** | Simple | Medium | **Complex** |
| **Resource Usage** | Low | Medium | **High** |
| **Interpretability** | Limited | High | **Medium** |
| **Training Required** | None | Medium | **Extensive** |

## 🗂️ Repository Structure

```
Movies-Recommendation/
│
├── 🌐 TMDB-API/
│   ├── app.py                 # Streamlit application
│   ├── imdb_movies.csv        # Movie dataset
│   ├── requirements.txt       # Dependencies
│   └── README.md              # API approach guide
│
├── 🧮 TFIDF-KNN/
│   ├── pickle_model/
│   │   ├── knn_model.pkl           # Trained KNN model
│   │   ├── tfidf_vectorizer.pkl    # TF-IDF vectorizer
│   │   └── movies_metadata.csv     # Processed dataset
│   ├── app.py                      # Streamlit application
│   ├── model.ipynb                 # Training notebook
│   ├── imdb_movies.csv            # Raw dataset
│   ├── requirements.txt           # Dependencies
│   └── README.md                  # ML approach guide
│
├── 🧠 Sentence-Transformer/    # 🚀 DEPLOYED VERSION
│   ├── saved_model/                # Fine-tuned transformer model
│   │   ├── 1_Pooling/
│   │   ├── config.json
│   │   ├── model.safetensors
│   │   ├── sentence_bert_config.json
│   │   └── ... (model files)
│   ├── movies_data.pkl             # Embeddings dataset
│   ├── app.py                      # Streamlit application
│   ├── model.ipynb                 # Training notebook
│   ├── imdb_movies.csv            # Raw dataset
│   ├── requirements.txt           # Dependencies
│   └── README.md                  # AI approach guide
│
└── 📖 README.md                   # This overview file
```

## 🎯 Which Approach Should You Choose?

### 🚀 **For Production Systems:**
- **High accuracy needed:** → Sentence Transformers
- **Real-time updates required:** → TMDB-API
- **Resource constraints:** → TF-IDF + KNN

### 📚 **For Learning:**
- **Understanding ML basics:** → TF-IDF + KNN  
- **API integration:** → TMDB-API
- **Modern AI/NLP:** → Sentence Transformers

### 💼 **For Business:**
- **Quick MVP:** → TMDB-API
- **Custom domain:** → TF-IDF + KNN
- **Premium product:** → Sentence Transformers

## 🛠️ Quick Start Guide

### Option 1: Try the Live Demo
```bash
# Visit the deployed Sentence Transformer app
https://movies-recommendation-using-sentence-transformer.streamlit.app/
```

### Option 2: Run Any Approach Locally
```bash
# Clone the repository
git clone https://github.com/u-faizan/Movies-Recommendation.git
cd Movies-Recommendation

# Choose your approach and navigate to folder
cd Sentence-Transformer  # or TMDB-API or TFIDF-KNN

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Option 3: Compare All Approaches
```bash
# Run each approach in different terminals
cd TMDB-API && streamlit run app.py --server.port 8501
cd TFIDF-KNN && streamlit run app.py --server.port 8502  
cd Sentence-Transformer && streamlit run app.py --server.port 8503
```

## 📈 Performance Insights

### **Recommendation Quality**
1. **🥇 Sentence Transformers** - Best semantic understanding
2. **🥈 TMDB-API** - Great crowd-sourced accuracy  
3. **🥉 TF-IDF + KNN** - Solid baseline performance

### **Speed & Efficiency**
1. **🥇 TMDB-API** - Instant API responses
2. **🥈 TF-IDF + KNN** - Fast local inference
3. **🥉 Sentence Transformers** - Slower but most accurate

### **Development Complexity**
1. **🥇 TMDB-API** - Just API integration
2. **🥈 TF-IDF + KNN** - Standard ML pipeline
3. **🥉 Sentence Transformers** - Advanced deep learning

## 🎓 Learning Path

### **Beginner → Intermediate → Advanced**

```
1. Start with TMDB-API 🌐
   ↓ Learn API integration & basic UI
   
2. Progress to TF-IDF + KNN 🧮  
   ↓ Understand ML fundamentals
   
3. Master Sentence Transformers 🧠
   ↓ Explore cutting-edge AI
```

## 🎨 Features Across All Apps

- **🎨 Modern UI Design** - Beautiful, responsive Streamlit interfaces
- **🖼️ Movie Posters** - Rich visual experience with TMDB integration
- **⚡ Smart Caching** - Optimized performance with intelligent caching
- **📱 Mobile Friendly** - Works seamlessly on all devices
- **🎯 15 Recommendations** - Consistent 5×3 grid layout
- **🔍 Smart Search** - Intuitive movie search and selection

## 🤝 Contributing

We welcome contributions to improve any of the three approaches!

1. **Fork the repository**
2. **Choose an approach** to enhance
3. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
4. **Commit your changes** (`git commit -m 'Add AmazingFeature'`)
5. **Push to the branch** (`git push origin feature/AmazingFeature`)
6. **Open a Pull Request**

### **Contribution Ideas:**
- 🎨 UI/UX improvements
- ⚡ Performance optimizations  
- 🧠 New ML approaches
- 📊 Evaluation metrics
- 🌍 Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **🎬 TMDB** - Comprehensive movie database and API
- **🤗 Hugging Face** - Pre-trained transformer models
- **📊 Streamlit** - Amazing web app framework
- **🧠 Sentence Transformers** - State-of-the-art NLP library
- **📚 Scikit-learn** - Reliable machine learning tools

## 📞 Support & Contact

- **📧 Issues:** [GitHub Issues](https://github.com/u-faizan/Movies-Recommendation/issues)
- **💬 Discussions:** [GitHub Discussions](https://github.com/u-faizan/Movies-Recommendation/discussions)
- **🔗 LinkedIn:** [Connect with me](https://linkedin.com/in/u-faizan)

---

### 🌟 **Star this repository if you found it helpful!**

**Built by Umar Faizan exploring the evolution of recommendation systems**

*From traditional ML to cutting-edge AI - experience the full spectrum of movie recommendation technologies!*
