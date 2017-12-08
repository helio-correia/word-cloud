import collections
import re
import requests
from bs4 import BeautifulSoup


def get_words_from_url(url):
    r = requests.get(url)
    text = get_text_from_url_content(r.content)
    text = remove_special_chars(text)
    word_list = text.split()
    word_counter = collections.Counter(word_list)
    print(dir(word_counter.most_common(100)))
    return word_counter.most_common(100)


def get_text_from_url_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    [s.extract() for s in soup('script')]  # Remove js scripts
    [s.extract() for s in soup('style')]  # Remove style scripts
    return soup.body.get_text()


def remove_special_chars(text):
    return re.sub(r'\\n|,|\(|\)|:|\.|/|º|ª|\|\'|[\[\]|]', ' ', text)
