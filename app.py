import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from textblob import TextBlob
import openai

# --- API Keys ---
SERPAPI_KEY = "cb77062e09a413a5156e5a92440ab298d05e33ddc00a551a852b240fca149f22"
NEWSAPI_KEY = "7271cff2fd6949f4b617adfa2f44d6d5"
OPENAI_API_KEY = "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"
REDDIT_CLIENT_ID = "Awkward_Ad_2832"
REDDIT_SECRET = "uhvXmNIpzP8vgEfsiyXoK4PrFsKyvg"
REDDIT_USER_AGENT = "InsightGenieBot/0.1"

# --- Page Config ---
st.set_page_config(page_title="InsightGenie", layout="wide")

st.sidebar.title('InsightGenie')
st.sidebar.markdown('Use the sidebar to navigate through the tool.')

# --- User Input ---
company_name = st.text_input('Enter a keyword or company name to analyze trends:')

if company_name:
    st.header(f"📊 Insights for {company_name}")

    # --- Keyword Trend (Mock Data or Replace with Google Trends API) ---
    st.subheader("📈 Keyword Trend")
    df = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=10),
        'Keyword Frequency': [12, 15, 10, 18, 20, 17, 23, 19, 25, 30]
    })
    fig = px.line(df, x='Date', y='Keyword Frequency', title=f'{company_name} Keyword Frequency Over Time')
    st.plotly_chart(fig)

    # --- Company Profiling using SerpAPI ---
    st.subheader("🏢 Company Profile")
    params = {"q": company_name, "api_key": SERPAPI_KEY}
    serp_response = requests.get("https://serpapi.com/search", params=params).json()
    if 'organic_results' in serp_response:
        for res in serp_response['organic_results'][:3]:
            st.write(f"**Title**: {res.get('title')}")
            st.write(f"**Snippet**: {res.get('snippet')}")
            st.write(f"**Link**: {res.get('link')}")
            st.markdown("---")
    else:
        st.write("No company info found.")

    # --- News Trend Tracker using NewsAPI ---
    st.subheader("📰 Trend Tracker (News)")
    news_url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={NEWSAPI_KEY}"
    news_response = requests.get(news_url).json()
    if news_response['status'] == 'ok':
        for article in news_response['articles'][:5]:
            st.write(f"**{article['title']}**")
            st.write(article['description'])
            st.write(article['url'])
            st.markdown("---")
    else:
        st.write("No news found.")

    # --- Sentiment Analysis (Reddit via PRAW) ---
    st.subheader("💬 Sentiment Analysis (Reddit)")
    try:
        import praw
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        posts = reddit.subreddit('all').search(company_name, limit=5)
        for post in posts:
            text = post.title + " " + post.selftext
            sentiment = TextBlob(text).sentiment.polarity
            label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
            st.write(f"**{post.title}** — Sentiment: {label}")
    except:
        st.write("Reddit API error. Check credentials or install praw.")

    # --- Survey Generator (OpenAI) ---
    st.subheader("📝 Custom Survey Generator")
    openai.api_key = OPENAI_API_KEY
    prompt = f"Generate 5 customer research survey questions for {company_name}. Focus on satisfaction, competitor analysis, and user needs."
    try:
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
        questions = completion.choices[0].text.strip().split('\n')
        for q in questions:
            st.write(f"- {q.strip('- ').strip()}")
    except:
        st.write("OpenAI API error. Check API key.")
