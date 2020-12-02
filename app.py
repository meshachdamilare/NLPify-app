import streamlit as st
#nltk pkg
import nltk
nltk.download('punkt')
nltk.download('wordnet')

from textblob import TextBlob
# gensim pkg
from gensim.summarization import summarize
# sumy pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def text_analyzer(my_text):
    blob = TextBlob(my_text)
    zen = blob.words
    all_data = ["Tokens: {}, \n Lemma: {}".format(z, z.lemmatize()) for z in zen]
    return all_data

def sumy_sumarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer('english'))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = " ".join(summary_list)
    return result

def main():

    st.title("NLP-ify with streamlit")
    st.subheader("Natural Language Processing on a go")

    # Tokenization
    if st.checkbox("Show Tokens and Lemmatization"):
        st.subheader("Tokenize your text")
        message = st.text_area("Enter Your Text", "Type Here", key = "1")
        if st.button("Analyze", key = "1"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)


    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Sentiment of Your Text")
        message = st.text_area("Enter Your Text", "Type Here", key = "2")
        if st.button("Analyze", key ='2'):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)

    # Text Summarization

    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Text")
        message = st.text_area("Enter Your Text", "Type Here", key = "3")
        summary = st.selectbox("Choose your summarizer", ('gensim', 'sumy'))
        if st.button("Summarize", key='3'):
            if summary == 'gensim':
                try:
                    st.text("Using Gensim...")
                    summary_result = summarize(message)
                    st.success(summary_result)
                except ValueError:
                    st.error("Input must have more than one sentence.")
            elif summary == 'sumy':
                try:
                    st.text("Using Sumy...")
                    summary_result = sumy_sumarizer(message)
                    st.success(summary_result)
                except:
                    st.error("Input correct things.")

    st.sidebar.subheader('About the App')
    st.sidebar.markdown('## NLP-ify App with Streamlit')
    st.sidebar.info("#### Get the Tokens of your text")
    st.sidebar.info("#### Get the Named-Entities of your text")
    st.sidebar.info("#### Get the Sentiment Analysis of your text")
    st.sidebar.info("#### Get the Summary of your text")
    
if __name__ == '__main__':
    main()
