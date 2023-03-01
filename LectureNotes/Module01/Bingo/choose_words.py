from collections import Counter
from nltk.corpus import stopwords
import string

DO_BOTH = True

def remove_punctuation(text: str) -> str:
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    return text

with open('content.txt') as f:
    text = f.read()
if DO_BOTH:
    text += " "
    with open('../01 Computational Thinking.md') as f:
        text += f.read()
text = remove_punctuation(text)
words = text.split()
lc = [word.lower() for word in words]
lc = [word for word in lc if word not in stopwords.words('english')]
lc = [word for word in lc if not word.isnumeric()]
lc = [word for word in lc if len(word) > 1]
c = Counter(lc)
for (w,ct) in c.most_common(20):
    print(w)

