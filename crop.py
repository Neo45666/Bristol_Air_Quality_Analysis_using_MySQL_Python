###  Name:                  Nelson Offor 
#### Module Code:           UFCFLR-15-M 
#### Module Title :         Data Management Fundamentals
#### Course:                Msc Data Science
#### Course work context:   Measuring Air Quality
#### Data to be analysed:   bistol-air-quality-data

#### import libraries and read in bristol air quality data file.
import csv
import pandas as pd
dataset = pd.read_csv('bristol-air-quality-data.csv',sep=';')
pd.to_datetime(dataset['Date Time'], format = '%Y-%m-%d')

dataset # view data 

#### Verify dataset dimension in rows and columns

dataset.shape

#### Verify dataset structure

dataset.info()

# Data Cleaning
#### Delete records before 00:00 1 Jan 2010.

dataset2 = dataset.loc[dataset['Date Time'] >= '2010-01-01']
dataset2

#### View dataset

dataset2.to_csv('crop.csv', index=False)