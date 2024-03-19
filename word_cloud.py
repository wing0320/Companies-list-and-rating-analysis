from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

stop_words = set(stopwords.words('english'))

def tokenize_and_remove_stopwords(text):
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return filtered_words

def create_word_clouds(df):
    highly_rated_text = ' '.join(df['highly_ratedFOR'])
    critically_rated_text = ' '.join(df['critically_ratedFOR'])

    if highly_rated_text:
        highly_rated_words = tokenize_and_remove_stopwords(highly_rated_text)
        highly_rated_freq = Counter(highly_rated_words)

        wordcloud = WordCloud(background_color='white').generate_from_frequencies(highly_rated_freq)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Word Cloud for Highly Rated Reviews")
        plt.show()
    else:
        print("No highly rated reviews found")

    if critically_rated_text:
        critically_rated_words = tokenize_and_remove_stopwords(critically_rated_text)
        critically_rated_freq = Counter(critically_rated_words)

        plt.figure(figsize=(10, 6))  # New figure for the second word cloud
        wordcloud = WordCloud(background_color='white').generate_from_frequencies(critically_rated_freq)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Word Cloud for Critically Rated Reviews")
        plt.show()
    else:
        print("No critically rated reviews found")

