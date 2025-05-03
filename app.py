import streamlit as st
import plotly.express as px
import pandas as pd

# Sidebar Setup
st.sidebar.title('InsightGenie')
st.sidebar.markdown('Use the sidebar to navigate through the tool.')

# Main content area
st.title('Welcome to InsightGenie')
st.markdown('Use the sidebar to choose your action.')

# Adding interactive functionality
st.header("Market Research")
keyword = st.text_input('Enter a keyword or company name to analyze trends:')
if keyword:
    st.write(f'Analyzing trends for: {keyword}')
    # Example: Replace with your real data or API calls
    data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'Keyword Frequency': [10, 12, 15]}
    df = pd.DataFrame(data)

    # Display a chart
    fig = px.line(df, x='Date', y='Keyword Frequency', title=f'{keyword} Keyword Frequency Over Time')
    st.plotly_chart(fig)

    # Add button for fetching mentions or news
    if st.button('Get Latest Mentions'):
        st.write(f'Fetching latest mentions of {keyword}...')
        # Add logic to call API (SerpAPI or NewsAPI) for fetching mentions.
