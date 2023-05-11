# Importing necessary libraries and modules
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# Initializing the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Loading the intents.json file
intents = json.loads(open('intents.json').read())

# Initializing empty lists and variables
words = []              # to store individual words
classes = []            # to store classes/tags
documents = []          # to store patterns and their corresponding intents
ignore_letters = ['?', '!', '.', ',']    # list of characters to ignore

# Processing the intents and extracting words and classes
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenizing the pattern into words
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)     # adding words to the words list
        documents.append((word_list, intent['tag']))    # storing pattern and intent tag
        if intent['tag'] not in classes:
            classes.append(intent['tag'])   # adding intent tag to classes if it's not already present

# Lemmatizing the words and removing ignore letters
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))    # sorting and removing duplicates

classes = sorted(set(classes))    # sorting classes

# Saving words and classes into pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Preparing the training data
training = []   # list to store training data
output_empty = [0] * len(classes)   # empty list for output

for document in documents:
    bag = []    # bag of words representation for each pattern
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)   # marking presence or absence of words in the pattern

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1   # one-hot encoding for the intent tag
    training.append([bag, output_row])    # appending bag of words and one-hot encoded output to the training data

random.shuffle(training)   # shuffling the training data
training = np.array(training)   # converting training data to numpy array

# Separating the features and labels from the training data
train_x = list(training[:, 0])    # features (bag of words)
train_y = list(training[:, 1])    # labels (intent tags)

# Building the model architecture
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compiling the model
sgd = SGD(learning_rate=0.01, weight_decay=1e-6, ema_momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Training the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print("Done")
