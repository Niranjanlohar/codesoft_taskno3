# Sample movie data
movies = [
    {"id": 1, "title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
    {"id": 2, "title": "Titanic", "genres": ["Romance", "Drama"]},
    {"id": 3, "title": "Inception", "genres": ["Action", "Thriller", "Sci-Fi"]},
    {"id": 4, "title": "The Notebook", "genres": ["Romance", "Drama"]},
    {"id": 5, "title": "Avengers: Endgame", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"id": 6, "title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"]}
]

# Sample user preferences
user_preferences = ["Sci-Fi", "Action"]

# Function to recommend movies based on genre overlap
def recommend_movies(movies, user_preferences, top_n=3):
    recommendations = []

    for movie in movies:
        # Count matching genres
        match_score = len(set(movie['genres']) & set(user_preferences))
        if match_score > 0:
            recommendations.append((movie['title'], match_score))

    # Sort by match score, descending
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:top_n]

# Get recommendations
recommended = recommend_movies(movies, user_preferences)

# Print the results
print("Recommended Movies:")
for title, score in recommended:
    print(f"{title} (match score: {score})")