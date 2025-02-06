import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def clean(Text):
    text = re.sub(r'@\w+', '', Text) # mention
    text = re.sub(r'\b(?:https?://|www\.)\S+\b', '', text) # url
    text = re.sub(r'#\w+', '', text) # hastag
    text = re.sub(r'\s+', ' ', text).strip() # space
    return text

sia = SentimentIntensityAnalyzer()

def sentiment_vader(text):
    compound_polarity = sia.polarity_scores(text)
    
    if compound_polarity['compound'] >= 0.05:
        return 'Positive'
    elif compound_polarity['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'>Input the Post</h2>", unsafe_allow_html=True)
    post = st.text_area('Enter the X Post:', 'Deepseek')

    with st.expander("Your Input"):
        result = {
            'Post': post,
        }

    # dataframe
    df = pd.DataFrame({'Post': [post]})

    # clean text
    df["clean_text"] = df["Post"].apply(clean)

    st.markdown("<h2 style = 'text-align: center;'> Your Post </h2>", unsafe_allow_html=True)

    st.write(post)

    # prediction section
    st.markdown("<h2 style = 'text-align: center;'> Analysis Result </h2>", unsafe_allow_html=True)

    df['Label'] = df['clean_text'].apply(lambda text: sentiment_vader(text))

    if df.iloc[0,2] == 'Positive':
        st.success("Positive Post")
        st.write('This is a positive sentiment post, please be careful in posting things on social media.')
    elif df.iloc[0,2] == 'Negative':
        st.error("Negative Post")
        st.write('This is a negative sentiment post, please be careful in posting things on social media.')
    else:
        st.warning('Neutral Post')
        st.write('This is a neutral sentiment post, please be careful in posting things on social media.')

    st.markdown('''<p style='text-align: justify;'> <br> <strong>Disclaimer:</strong> This tool is only to help analyze and may analyze sentiments incorrectly. Perform further analysis to reduce analysis errors.</p>''', unsafe_allow_html=True)