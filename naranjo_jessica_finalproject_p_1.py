# -*- coding: utf-8 -*-
"""Naranjo_Jessica_FinalProject_p#1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Dx0J7zCJdV21Sc6qDtJP9xUnZePgeQx
"""



from google.colab import drive
drive.mount("/content/drive")

import pandas as pd

df = pd.read_csv('/content/drive/My Drive/FinalProject/chineseMNIST.csv')

df.head()

import random
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.metrics import confusion_matrix
from  sklearn.model_selection import train_test_split

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from keras.utils import np_utils
from tensorflow.keras.utils import to_categorical

import matplotlib
import matplotlib.pyplot as plt

#1.	Read the dataset into a dataframe. (1)
import pandas as pd
letter_df = pd.read_csv('/content/drive/My Drive/FinalProject/chineseMNIST.csv')
print(letter_df.head())

import matplotlib.font_manager as font_manager

# Add every font at the specified location
font_dir = ['/content/drive/MyDrive/FinalProject/font']
for font in font_manager.findSystemFonts(font_dir):
  print("font font is",font)
  font_manager.fontManager.addfont(font)

#2.	Explore the dataset and determine what is the target variable. (1)
    #the target variabe is the correct letter label
matplotlib.rc('font', family='SimHei')
d={}
#3.	Separate the dataframe into feature set and target variable. (1)
X= letter_df.iloc[:,:-2]  #feature set
y= letter_df.iloc[:,-2]  #target variable
z=letter_df.iloc[:,-1]
print("this is y", y)

#4.	Print the shape of feature set and target variable. (1)
print("shape of the feature set:", X.shape)
print("shape of the target variable:", y.shape)

#5.	Is the target variable values letters or numbers? (1)
    #it is numbers

#6.	If it is numbers, then how would you map numbers to letters? Hint: Use a data dictionary (1)
final ={}
for a,b in enumerate(zip(letter_df.iloc[:,-2],letter_df.iloc[:,-1].values)):
  final[b[0]]=b[1]

d=dict(sorted(final.items()))
i=0
word_dict={}
for key in d.keys():
  word_dict[i]=final[key]
  i=i+1
word_dict


#7.	Show a histogram (count) of the letters. (1)

plt.figure(1)
hist = sb.countplot(x = "label", data=letter_df)
hist.set_xticklabels(word_dict.values())
plt.show()

#8.	Display 25 random letters from the dataset. 
plt.figure(figsize=[10,10])
import random
plt.rcParams["font.serif"] = "cmr10"
random_numbers=list(random.sample(range(0, len(letter_df)), 25))
for i in range(25):
    j=random_numbers[i]
    letter = X.iloc[j, :]
    letter_name = y[j]
    chinese_letter_name = z[j]
    letter = np.array(letter)
    letter = letter.reshape(64,64)
    plt.subplot(8,8,i+1).imshow(letter)
    plt.subplot(8,8,i+1).set_title("True: %s" %letter_name)
    plt.text(8, 76, "Pred: %s" %chinese_letter_name)
    plt.subplot(8,8, i+1).axis('off')

plt.subplots_adjust(hspace=1)

plt.show()

letter_df.columns

from collections import Counter

d=dict(sorted(dict(Counter(letter_df['label'].values)).items()))
i=0
for each_key in d:
  d[each_key]=i
  i=i+1
letter_df['label'] = letter_df['label'].map(d)


X= letter_df.iloc[:,:-2]  #feature set
y= letter_df.iloc[:,-2]  #target variable

X = X / 255.0
X = X.values
X=X.reshape(-1,64,64,1)

Y = letter_df['label']
# y = to_categorical(Y, num_classes = 15)
X_train, X_test, Y_train, Y_test =train_test_split(X,Y, test_size=0.30, random_state=2022, stratify = y)

word_dict

print("Shape of X_Train and Y_Train ", X_train.shape,Y_train.shape)
print("Shape of X_Test and Y_Test ", X_test.shape,Y_test.shape)

from tensorflow.keras import layers

model = Sequential()

model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu',
                        input_shape=(64, 64, 1)))
model.add(layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
model.add(layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
model.add(layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
model.add(layers.Flatten())

model.add(layers.Dense(units=1024, activation='relu'))
model.add(layers.Dense(units=512, activation='relu'))
model.add(layers.Dense(units=256, activation='relu'))
model.add(layers.Dense(units=15, activation='softmax'))


model.summary()

model.compile(loss= 'sparse_categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
#model.compile(loss= 'categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
history = model.fit(X_train, Y_train, batch_size=64, epochs=25, validation_data=(X_test, Y_test))

# plot the validation and training accuracy
fig, axis = plt.subplots(1, 2, figsize=(16,6))
axis[0].plot(history.history['val_accuracy'], label='val_acc')
axis[0].set_title("Validation Accuracy")
axis[0].set_xlabel("Epochs")
axis[1].plot(history.history['accuracy'], label='acc')
axis[1].set_title("Training Accuracy")
axis[1].set_xlabel("Epochs")
plt.show()

# plot the validation and training accuracy
fig, axis = plt.subplots(1, 2, figsize=(16,6))
axis[0].plot(history.history['loss'], label='Train_loss')
axis[0].set_title("Training Loss")
axis[0].set_xlabel("Epochs")
axis[1].plot(history.history['val_loss'], label='val_loss')
axis[1].set_title("Validation Loss")
axis[1].set_xlabel("Epochs")
plt.show()

word_dict

#10Visualize the predicted and actual image labels for the first 30 images in the dataset.


#predict
pred = model.predict(X_test)

#convert the rpedictions into label index
pred_classes = np.argmax(pred, axis=1)
y_test=list(Y_test)
#plot the actual vs predicted results
plt.figure(figsize=[10,10])
for i in range(30):
    letter=X_test[i]
    letter=letter.reshape(64,64)
    plt.subplot(5,6,i+1).imshow(letter)
    plt.subplot(5,6,i+1).set_title("True: %s" %word_dict[y_test[i]])
    plt.text(18, 76, "Pred: %s" %word_dict[pred_classes[i]])
    plt.subplot(5,6, i+1).axis('off')
plt.subplots_adjust(hspace=1)
plt.show()

#convert the rpedictions into label index
#plot the actual vs predicted results
plt.figure(figsize=[10,10])
j=0
while j!=30:
  if y_test[i]!=pred_classes[i]:
    letter=X_test[i]
    letter=letter.reshape(64,64)
    plt.subplot(5,6,j+1).imshow(letter)
    plt.subplot(5,6,j+1).set_title("True: %s" %word_dict[y_test[i]])
    plt.text(18, 76, "Pred: %s" %word_dict[pred_classes[i]])
    plt.subplot(5,6, j+1).axis('off')
    j=j+1
  else:
    i=i+1
plt.subplots_adjust(hspace=1)
plt.show()