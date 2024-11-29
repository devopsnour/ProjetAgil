from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movie data
movies = [
    {"id": 1, "title": "Movie 1", "image": "images/22.png"},
    {"id": 2, "title": "Movie 2", "image": "images/20.png"},
    {"id": 3, "title": "Movie 3", "image": "images/8.png"},
    {"id": 4, "title": "Movie 4", "image": "images/2.png"},
    {"id": 5, "title": "Movie 5", "image": "images/10.png"}
]

@app.route('/')
def home():
    return render_template('home.html', movies=movies)

@app.route('/recommendations')
def recommendations():
    # Placeholder for recommendations
    return render_template('recommendations.html')

@app.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'POST':
        movie_id = request.form.get('movie_id')
        rating = request.form.get('rating')
        # Save the rating (this example just prints it)
        print(f"Movie ID: {movie_id}, Rating: {rating}")
        return redirect(url_for('home'))
    movie_id = request.args.get('movie_id', '')
    return render_template('rate.html', movie_id=movie_id)

if __name__ == '__main__':
    app.run(debug=True)
