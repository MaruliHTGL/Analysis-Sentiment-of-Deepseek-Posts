import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Post Analysis']
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Home':
        st.markdown(
            """
            <h1 style='text-align: center;'>
                Deepseek Sentiment Analyzer
                Uncover the True Public Opinion!
            </h1>
            
            <br>

            <p style='text-align: justify;'>
                In the fast-paced world of social media, opinions shape reputations. But what are people on X (formerly Twitter) really saying about <strong>Deepseek</strong>? Is the sentiment <strong>positive</strong>, <strong>negative</strong>, or <strong>neutral</strong>? Instead of scrolling through countless posts, let Deepseek Sentiment Analyzer do the work for you.
            </p>

            <br>

            <h3 style='text-align: justify;'>Why Use Deepseek Sentiment Analyzer?</h3>
            <ul>
                <li><strong>Instant Sentiment Analysis:</strong> Gain quick insights into public perception with AI-powered analysis.</li>
                <li><strong>Data-Driven Decisions:</strong> Understand trends, measure reactions, and make informed choices based on real-time data.</li>
                <li><strong>Track Public Opinion Over Time:</strong> Monitor how discussions evolve and respond proactively.</li>
                <li><strong>Identify Opportunities & Risks:</strong> Spot emerging trends, detect potential PR crises, and engage with your audience more effectively.</li>
            </ul>

            <br>

            <p style='text-align: justify;'>
                Whether you're a business, researcher, or social media analyst, knowing what people think about Deepseek has never been easier. Stay ahead of the conversation and make smarter decisions with real-time sentiment analysis.
            </p>
            
            <br>

            <p style='text-align: justify;'>
                <strong>Disclaimer:</strong> This tool is only to help analyze and may analyze sentiments incorrectly. Perform further analysis to reduce analysis errors
            </p>

            <br>

            <p style='text-align: center;'>
                <strong>Start analyzing now and uncover valuable insights!</strong>
            </p>
            """, 
            unsafe_allow_html=True
        )

    elif choice == "Post Analysis":
        run_ml_app()

if __name__ == '__main__':
    main()
