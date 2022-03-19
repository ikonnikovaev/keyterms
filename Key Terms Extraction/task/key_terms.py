# Write your code here
import string

import nltk
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

stopwords_list = stopwords.words('english')
punct_list = list(string.punctuation)
#print(punct_list)

def extract_nouns(story_text):
    tokens = word_tokenize(story_text)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    filtered_lemmas = [lemma for lemma in lemmas
                       if lemma not in stopwords_list and lemma not in punct_list]
    # print(nltk.pos_tag(filtered_lemmas))
    # print([(lemma, nltk.pos_tag([lemma])[0][1]) for lemma in filtered_lemmas])

    nouns = [lemma for lemma in filtered_lemmas
             if nltk.pos_tag([lemma])[0][1] == "NN"]
    return nouns

def find_frequent(story_text, k=5):
    nouns = extract_nouns(story_text)
    freq_counter = Counter(sorted(nouns, reverse=True))
    most_common_nouns = sorted(freq_counter.most_common(k),
                                key=lambda x: (x[1], x[0]), reverse=True)
    return [noun[0] for noun in most_common_nouns]

def find_important(dataset, k=5):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(dataset)
    feature_array = np.array(vectorizer.get_feature_names_out())
    important_words = []
    for i in range(len(dataset)):
        tfidf_arr = tfidf_matrix[i].toarray().flatten()
        tfidf_sorting = np.argsort(tfidf_arr, kind='stable')[::-1]
        important_words.append(feature_array[tfidf_sorting][:k])
    return important_words

stories = {}
xml_path = "news.xml"
lemmatizer = WordNetLemmatizer()
tree = etree.parse(xml_path)
root = tree.getroot()
corpus = root[0]

headlines = []
preprocessed_texts = []

for news in corpus:
    headlines.append(news[0].text)
    story_text = news[1].text.lower()
    preprocessed_texts.append(' '.join(extract_nouns(story_text)))

keywords = find_important(preprocessed_texts)
for (headline, keywords) in zip(headlines, keywords):
    print(f'{headline}:')
    print(' '.join(keywords))






