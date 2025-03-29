from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__, template_folder="templates")

book_list = pickle.load(open('books.pkl','rb'))
similarity = pickle.load(open("similarity.pkl", "rb"))


# Recommendation function
def recommend(book_title):
    if book_title not in book_list["title"].values:
        return []

    index = book_list[book_list["title"] == book_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5 recommendations
    recommended_books = book_list.iloc[[i[0] for i in scores]][["title", "thumbnail"]].to_dict(orient="records")

    return recommended_books

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET','POST'])
def get_recommendations():
    book_title = request.form['title']
    recommendations = recommend(book_title)
    return render_template('index.html', recommendations=recommendations, book_title=book_title)


if __name__ == '__main__':
    app.run(debug=True)
