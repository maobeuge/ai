import pandas as pd
import random


###### Création des Datasets

data_dir_train = 'digit-recognizer/train.csv'
data_dir_test = 'digit-recognizer/test.csv'
categories = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
img_size = 28


### Dataset train

dataTrain = pd.read_csv(data_dir_train)

dataTrain = dataTrain.sample(frac=1).reset_index(drop=True)

yTrain = dataTrain['label']
xTrain = dataTrain.drop(columns=['label'])


### Dataset test

dataTest = pd.read_csv(data_dir_test)

yTest = dataTest['label']
xTest = dataTest.drop(columns=['label'])


###### Entraînement du model

