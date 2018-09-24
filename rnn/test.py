import os
import string
from bs4 import BeautifulSoup

files = os.walk(os.path.join(os.path.dirname(__file__), '..', 'output'))

raw_text = ''
raw_array = []
translator = str.maketrans('','', string.punctuation)
for dirpath, dirnames, filenames in files:
    for name in filenames:
        with open(os.path.join(dirpath, name), encoding='utf-8') as html:
             soup = BeautifulSoup(html)
             for script in soup(["script", "style"]):
                 script.extract()
             

             trimmed = [" ".join(s.strip().translate(translator).split()) 
                     for s in list(soup.stripped_strings)]
             raw_text += '\n'.join(list(filter(bool, trimmed)))

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
n_chars = len(raw_text)
n_vocab = len(chars)

print('Total Characters: {}'.format(n_chars))
print('Total vocab: {}'.format(n_vocab))
