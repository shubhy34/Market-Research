import streamlit as st
import openai
import os
from modules.openai_utils import generate_company_summary
from modules.scraper import scrape_company_info
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="InsightGenie - Competitor Profile", layout="wide")
st.title("📊 Competitor Profile")

company_name = st.text_input("Enter Company Name", "OpenAI")

if st.button("Analyze"):
    with st.spinner("Scraping company data and generating insights..."):
        scraped_data = scrape_company_info(company_name)
        summary = generate_company_summary(scraped_data)

    st.subheader("🔍 Summary")
    st.write(summary)

    st.subheader("📋 Raw Data")
    st.json(scraped_data)
