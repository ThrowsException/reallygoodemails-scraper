import os
import numpy
import string
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from bs4 import BeautifulSoup

files = os.walk(os.path.join(os.path.dirname(__file__), '..', 'output'))
translator = str.maketrans('','', string.punctuation)

raw_text = ''
for dirpath, dirnames, filenames in files:
    for name in filenames:
        with open(os.path.join(dirpath, name), encoding='utf-8') as html:
             soup = BeautifulSoup(html)
             for script in soup(["script", "style"]):
                 script.extract()
             
             trimmed = [" ".join(s.strip().translate(translator).split()) 
                     for s in list(soup.stripped_strings)]
             raw_text += '\n'.join(list(filter(bool, trimmed)))

raw_text = raw_text.lower()
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
n_chars = len(raw_text)
n_vocab = len(chars)

print('Total Characters: {}'.format(n_chars))
print('Total vocab: {}'.format(n_vocab))

# prepare the dataset of input to output pairs
seq_length = 5 
dataX = []
dataY = []

for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

n_patterns = len(dataX)
print('Total Patterns: {}'.format(n_patterns))

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# define the checkpoint
filepath="/tmp/weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(X, y, epochs=50, batch_size=32, callbacks=callbacks_list)
