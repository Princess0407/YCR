import streamlit as st
from model.recommender import YouTubeRecommender

# Title
st.title("🎬 YouTube Content Recommender")
st.write("Get video recommendations based on your favorite videos!")

# Theme toggle
theme = st.sidebar.radio("Choose Theme", ["Dark", "Light"])

# CSS for dark theme
if theme == "Dark":
    css_file = "assets/style.css"
else:
    css_file = "assets/style_light_theme.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load model
recommender = YouTubeRecommender("data/complete_youtube_recommendation_dataset.csv")

# Input field
video_title = st.text_input("Enter a video title:")

if st.button("Recommend"):
    if video_title.strip():
        title, recs = recommender.recommend(video_title)
        if isinstance(recs, list) and recs:
            st.subheader(f"If you liked: *{title}*")
            st.write("You might also like:")
            for name, score in recs:
                st.markdown(f"- **{name}** *(similarity: {score:.2f})*")
        else:
            st.error(recs)
    else:
        st.warning("Please enter a video title.")
