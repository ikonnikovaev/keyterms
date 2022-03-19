# Write your code here
import string

import nltk
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

stopwords_list = stopwords.words('english')
punct_list = list(string.punctuation)
#print(punct_list)

def extract_common_words(story_text, k=5):
    tokens = word_tokenize(story_text)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    filtered_lemmas = [lemma for lemma in lemmas
                       if lemma not in stopwords_list and lemma not in punct_list]
    nouns = [lemma for lemma in filtered_lemmas
             if nltk.pos_tag([lemma])[0][1] == "NN"]

    freq_counter = Counter(sorted(nouns, reverse=True))
    most_common_nouns = sorted(freq_counter.most_common(k),
                                key=lambda x: (x[1], x[0]), reverse=True)
    return [noun[0] for noun in most_common_nouns]


# stories = {}
xml_path = "news.xml"
lemmatizer = WordNetLemmatizer()
tree = etree.parse(xml_path)
root = tree.getroot()
corpus = root[0]
for news in corpus:
    headline = news[0].text
    story_text = news[1].text.lower()
    most_common_words = extract_common_words(story_text, k=5)
    print(headline +':')
    print(' '.join(most_common_words))





