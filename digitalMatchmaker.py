import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
vocabulary = ["python", "cloud", "automation", "web-design", "algorithms"]

items = {
    "Course A": [1, 2, 0, 0, 1],  # Heavy focus on Python, Cloud, and Algorithms
    "Course B": [0, 0, 2, 2, 0],  # Heavy focus on Automation and Web Design
    "Course C": [2, 1, 0, 0, 0]   # Focus on Python and Cloud
}

# 3.User Profile (Input - User State)
user_interests = [1, 1, 0, 0, 0] # User is interested in Python and Cloud [cite: 72, 93]

# 4. Process: To Calculate Similarity
def get_recommendations(user_profile, item_data):
    user_vec = np.array(user_profile).reshape(1, -1)
    recommendations = []
    
    for name, vector in item_data.items():
        item_vec = np.array(vector).reshape(1, -1)
        score = cosine_similarity(user_vec, item_vec)[0][0]
        recommendations.append((name, score))
    
    #Top-N List:-
    return sorted(recommendations, key=lambda x: x[1], reverse=True)

# 5. Output: Display recommended items
results = get_recommendations(user_interests, items)
print("Top Recommendations:")
for item, score in results:
    print(f"{item}: Similarity Score {score:.2f}")