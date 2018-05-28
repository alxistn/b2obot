# Importing dependencies

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import RNN
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint


# Loading data

text = (open("LyricsGenius/Lyrics_Booba.txt").read())
#text = (open("debug.txt").read())
text=text.lower()


# Creating character/word mapping

characters = sorted(list(set(text)))

n_to_char = {n:char for n, char in enumerate(characters)}
char_to_n = {char:n for n, char in enumerate(characters)}


# Data preprocessing

X = []
Y = []
length = len(text)
seq_length = 100

for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label =text[i + seq_length]
    X.append([char_to_n[char] for char in sequence])
    Y.append(char_to_n[label])

X_modified = np.reshape(X, (len(X), seq_length, 1))
X_modified = X_modified / float(len(characters))
Y_modified = np_utils.to_categorical(Y)


# A gigantic model

model = Sequential()
model.add(LSTM(700, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(700, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(700))
model.add(Dropout(0.2))
model.add(Dense(Y_modified.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam',  metrics=['accuracy'])

# checkpointPath = "weights-improvement-{epoch:02d}-{acc:.2f}.h5"
# checkpoint = ModelCheckpoint(checkpointPath, monitor='acc', save_best_only=True, mode='max', period=1)

# callbacks_list = [checkpoint]

# model.fit(X_modified, Y_modified, epochs=100, batch_size=150, callbacks=callbacks_list)

# model.save_weights('text_generator_gigantic.h5')

model.load_weights('text_generator_gigantic.h5')


# Generating text

def make_prediction(length):
    print ("########## " + `length` + " ##########")
    string_mapped = X[np.random.randint(0, len(X) - 1)]
    full_string = [n_to_char[value] for value in string_mapped]
    print ("Seed: " + ''.join(full_string) + " ----------\n")
    # generating characters
    for i in range(length):
        x = np.reshape(string_mapped,(1,len(string_mapped), 1))
        x = x / float(len(characters))

        pred_index = np.argmax(model.predict(x, verbose=0))
        seq = [n_to_char[value] for value in string_mapped]
        full_string.append(n_to_char[pred_index])

        string_mapped.append(pred_index)
        string_mapped = string_mapped[1:len(string_mapped)]


    # Combining text
        
    txt=""
    for char in full_string:
        txt = txt+char
    print (txt)


for i in range(100):
    make_prediction(144)

