# Write your code here
from lxml import etree
from nltk.tokenize import word_tokenize
from collections import Counter
'''
root = (etree.parse("news.xml")).getroot()
for n in range(len(root[0])):
    print(root[0][n][0].text, ":", sep="")
    most_freq = Counter(word_tokenize(root[0][n][1].text.lower())).most_common()
    sorted_list = sorted(most_freq, key=lambda item: (item[1], item[0]), reverse=True)
    for i in range(5):
        print(sorted_list[i][0], end=" ")
    print("\n")
'''
stories = {}
xml_path = "news.xml"
tree = etree.parse(xml_path)
root = tree.getroot()
corpus = root[0]
for news in corpus:

    headline = news[0].text
    story_text = news[1].text.lower()
    words = word_tokenize(story_text)
    freq_counter = Counter(sorted(words, reverse=True))
    most_common_tokens = sorted(freq_counter.most_common(5),
                                key=lambda x: (x[1], x[0]), reverse=True)
    print(headline +':')
    print(' '.join([t[0] for t in most_common_tokens]))





