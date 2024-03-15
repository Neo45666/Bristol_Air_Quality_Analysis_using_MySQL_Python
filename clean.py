# This script generates a clean file.
### To import cropped data for cleaning 

import csv
import pandas as pd
import numpy as np
dataset2=pd.read_csv('crop.csv', low_memory=False)

### reset index of data

mask = dataset2[['SiteID','Location']]
mask.drop_duplicates().reset_index(drop=False)

### Arrange schema in a list

clean_data=[
['188','AURN Bristol Centre'], ['203','Brislington Depot'], ['206','Rupert Street'], ['209','IKEA M32'],
['213','Old Market'],['215','Parson Street School'], ['228','Temple Meads Station'], ['270','Wells Road'],
['271','Trailer Portway P&R'], ['375','Newfoundland Road Police Station'], ['395',"Shiner's Garage"], 
['452','AURN St Pauls'], ['447','Bath Road'], ['459','Cheltenham Road \ Station Road'], ['463','Fishponds Road'],
['481','CREATE Centre Roof'], ['500','Temple Way'], ['501','Colston Avenue']]

clean_data = pd.DataFrame(clean_data, columns = ['SiteID', 'Location'])
clean_data['Site_location'] = clean_data['SiteID'] +','+ clean_data['Location']
print(clean_data)

# creating third column to check for similarities to check mismatch

dataset2['Site_location']=dataset2['SiteID'].astype(str)+','+dataset2['Location']
dataset2

# finding mismatch lines 

find_mismatch={'Line Number':[i for i, x in enumerate(dataset2['Site_location'].tolist())  if x  not in clean_data['Site_location']
 .tolist()],'Mismatched line': [[x] for i, x in enumerate(dataset2['Site_location'].tolist()) 
if x not in clean_data['Site_location'].tolist()]}

mis_match_records= pd.DataFrame(find_mismatch)
mis_match_records

### record mismatch detected

mis_rec = mis_match_records['Mismatched line'].value_counts()
mis_rec

# Detect line numbers showing mismatch data 

recData = mis_match_records['Line Number']
dataset2.drop(dataset2.index[recData], inplace = True)
dataset2

#Drop the inserted 24th column showing the mismatch 

dataset2 = dataset2.drop(columns=['Site_location'])

dataset2.head()

#produce clean csv file 

dataset2.to_csv('clean.csv', index=False)