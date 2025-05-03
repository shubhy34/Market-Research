import streamlit as st
import os
from dotenv import load_dotenv
from modules.openai_utils import extract_keywords
from modules.visualizer import plot_keyword_frequency
from modules.trends import fetch_google_trends
from modules.news import fetch_company_news

load_dotenv()

st.set_page_config(page_title="Keyword & Trend Analysis", layout="wide")
st.title("📈 Keyword & Trend Analysis")

summary_input = st.text_area("Paste Company Summary / Description")

if st.button("Extract Keywords and Analyze"):
    with st.spinner("Processing..."):
        keywords = extract_keywords(summary_input)
        keyword_list = [k.strip() for k in keywords.split(',') if k.strip()]
        st.subheader("🧠 Extracted Keywords")
        st.write(keyword_list)

        st.subheader("🌍 Google Trends")
        trend_data = fetch_google_trends(keyword_list)
        st.plotly_chart(plot_keyword_frequency(trend_data))

        st.subheader("📰 Latest News")
        for kw in keyword_list[:3]:  # show top 3 keyword-related news
            news = fetch_company_news(kw)
            st.markdown(f"### {kw}")
            for article in news:
                st.markdown(f"- [{article['title']}]({article['link']})")
