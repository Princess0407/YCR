# YouTube Content Recommender (Static Version)

This project is a simple YouTube content recommender built to understand how recommendation systems work at a basic level.  
The system uses a structured dataset stored in a CSV file and recommends videos based on user preferences such as topic or interest.

The focus of this project is on building clear recommendation logic rather than using complex machine learning models.  
The application is implemented using Streamlit to provide an interactive and easy to use interface.

---

## What the Project Does

- Accepts user input like topic or area of interest  
- Reads a predefined CSV dataset containing YouTube video information  
- Filters and ranks videos using rule based logic  
- Displays relevant video recommendations through a web interface  

All recommendations are generated using explicit conditions and scoring rules defined in the code.

---

## About the Recommendation Approach

This recommender is **data driven but not machine learning based**.

Although a CSV dataset is used, the system does not learn patterns automatically from data. The recommendation logic is written manually and remains the same unless the code is changed.

This approach was chosen intentionally to:

- Understand the fundamentals of recommender systems  
- Keep the logic transparent and easy to debug  
- Avoid treating machine learning as a black box  
- Build a strong base before moving to adaptive systems  

---

## Tech Stack

- Python  
- Streamlit  
- CSV based dataset  
- Rule based filtering and scoring  

---

## How to Run the Streamlit App

### Step 1: Clone the repository

```bash
git clone <repo-url>
cd <project-folder>
```
### Step 2: Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate        # Linux or macOS
venv\Scripts\activate           # Windows
```

### Step 3: Install dependencies
```
pip install -r requirements.txt
```

### Step 4: Run the application
```
streamlit run app.py
```

The app will open in your browser, usually at:
```
http://localhost:8501
```

*Some improvements I plan on making in near future:*

- Making recommendations dynamic instead of fully rule based
- Using user interaction and feedback for ranking
- Introducing basic learning or adaptive weighting
- Improving recommendation quality over time
- Expanding the dataset and adding persistent user data
- Introdcuig mood based recommendation 
