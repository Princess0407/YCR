import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class YouTubeRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['text'] = (
            self.df['title'].fillna('') + ' ' +
            self.df['description'].fillna('') + ' ' +
            self.df['keywords'].fillna('')
        )
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['text'])

    def recommend(self, video_title, top_n=5):
        try:
            idx = self.df[self.df['title'].str.lower() == video_title.lower()].index[0]
        except IndexError:
            return f"No video found with title: {video_title}", []

        cosine_similarities = cosine_similarity(
            self.tfidf_matrix[idx], self.tfidf_matrix
        ).flatten()
        related_indices = cosine_similarities.argsort()[::-1][1:top_n + 1]

        recommendations = [
            (self.df.iloc[i]['title'], cosine_similarities[i])
            for i in related_indices
        ]
        return self.df.iloc[idx]['title'], recommendations


# test block
if __name__ == "__main__":
    recommender = YouTubeRecommender("data/complete_youtube_recommendation_dataset.csv")
    video, recs = recommender.recommend("An experimental new way to design software")
    print(f"If you liked: {video}\n")
    print("You might also like:")
    for title, score in recs:
        print(f" - {title} ({score:.2f})")
