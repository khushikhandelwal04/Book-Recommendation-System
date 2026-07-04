# 📚 Book Recommendation System

A content-based book recommendation web app built with **Flask**. Enter a book title, and it suggests similar books based on title, author, and category — powered by a precomputed similarity model.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Flask](https://img.shields.io/badge/Flask-Web%20App-black) ![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange)

---

## 🔍 Overview

This project recommends books similar to one you already like. It's a **content-based filtering** system — meaning recommendations are based on the *characteristics of the books themselves* (title, author, category), not on other users' ratings or behavior.

Built as a college project to practice applying machine learning concepts (vectorization + similarity scoring) inside a real, usable web application.

## ✨ Features

- 🔎 Search for any book title from the dataset
- 🎯 Get the **top 5 most similar books** instantly
- 🖼️ Results shown with book thumbnails
- 🌙 Modern dark-mode UI
- ⚡ Fast lookups using a precomputed similarity matrix (no real-time model training needed)

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML / Data | Pandas, scikit-learn |
| Frontend | HTML, CSS |
| Model storage | Pickle (`.pkl`) |

## ⚙️ How It Works

1. Book metadata (title, author, category, thumbnail) is preprocessed and stored in `books.pkl`.
2. A similarity matrix is precomputed (using `scikit-learn`, likely cosine similarity over vectorized book features) and stored in `similarity.pkl`.
3. When a user submits a book title via the form:
   - The app finds that book's index in the dataset.
   - It looks up the corresponding row in the similarity matrix.
   - It sorts scores in descending order and returns the top 5 closest matches.
4. Results (titles + thumbnails) are rendered back on the same page.

## 📁 Project Structure

```
Book-Recommendation-System/
├── app.py                 # Flask app + recommendation logic
├── books.pkl              # Preprocessed book data
├── similarity.pkl         # Precomputed similarity matrix (see note below)
├── requirements.txt       # Python dependencies
├── static/
│   └── CSS/                # Stylesheets
└── templates/              # HTML templates
```

> ⚠️ **Note:** `app.py` requires `similarity.pkl` to run, but this file isn't in the repo — it's a precomputed matrix comparing every book to every other book, and was likely too large to upload to GitHub. The original notebook/script used to generate it is also no longer available. To make this repo fully runnable again, the similarity matrix would need to be rebuilt from `books.pkl` (e.g. vectorizing title/author/category with `CountVectorizer` or `TfidfVectorizer`, then computing cosine similarity) and re-added — ideally via [Git LFS](https://git-lfs.com/) or hosted externally, since it's a large file.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/khushikhandelwal04/Book-Recommendation-System.git
cd Book-Recommendation-System

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## 🔮 Future Improvements

- Add collaborative filtering as a hybrid recommendation layer
- Deploy live (e.g. Render/Railway) for a public demo
- Add search-as-you-type / autocomplete for book titles
- Expand dataset size for broader coverage

## 👩‍💻 Author

**Khushi Khandelwal**
Built as a college project to explore machine learning applied to real-world recommendation systems.
