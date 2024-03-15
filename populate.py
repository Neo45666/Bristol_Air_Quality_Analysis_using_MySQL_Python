# python script to populate Database

import csv
import pandas as pd
import mysql.connector
dbconn = mysql.connector.connect(host="localhost",port=3306,password="",
                             user="root", database="pollution-db2")
mycursor=dbconn.cursor()
#print(dbconn)

### check server connection
if (dbconn):
    print("Successfully connected to server")
else:
    print(" Cannot connect to server")
  
### create datebase   
mycursor.execute("CREATE DATABASE IF NOT EXISTS `pollution-db2`")

mycursor.execute("USE `pollution-db2`")

### Create table in site table database
sit_sql= """ CREATE TABLE IF NOT EXISTS site(`SiteID` int(10) NOT NULL,`Location` varchar(100) DEFAULT NULL,`geo_point_2d` varchar(100) DEFAULT NULL,
   PRIMARY KEY(`SiteID`));"""
mycursor.execute(sit_sql)

### create readings table
rea_sql=""" CREATE TABLE IF NOT EXISTS readings(`ReadingsID` int(11) NOT NULL AUTO_INCREMENT,`Date Time` datetime DEFAULT NULL,
  `NOx` varchar(45) DEFAULT NULL,
  `NO2` varchar(45) DEFAULT NULL,
  `NO` varchar(45) DEFAULT NULL,
  `SiteID` int(11) DEFAULT NULL,
  `PM10` varchar(45) DEFAULT NULL,
  `NVPM10` varchar(45) DEFAULT NULL,
  `VPM10` varchar(45) DEFAULT NULL,
  `NVPM2.5` varchar(45) DEFAULT NULL,
  `PM2.5` varchar(45) DEFAULT NULL,
  `VPM2.5` varchar(45) DEFAULT NULL,
  `CO` varchar(45) DEFAULT NULL,
  `O3` varchar(45) DEFAULT NULL,
  `SO2` varchar(45) DEFAULT NULL,
  `Temperature` varchar(45) DEFAULT NULL,
  `RH` varchar(45) DEFAULT NULL,
  `Air pressure` varchar(45) DEFAULT NULL,
  `DateStart` varchar(45) DEFAULT NULL,
  `DateEnd` varchar(45) DEFAULT NULL,
  `Current` varchar(45) DEFAULT NULL,
  `Instrument Type` varchar(45) DEFAULT NULL,
   PRIMARY KEY (`ReadingsID`));"""
mycursor.execute(rea_sql)

### create schema table

sch_sql = """ CREATE TABLE IF NOT EXISTS `schema`(`measure` varchar(100) NOT NULL,`Desc` varchar(100) DEFAULT NULL, `Unit` varchar(45) DEFAULT NULL, PRIMARY KEY(measure));"""
mycursor.execute(sch_sql)

### to load site table drop duplicate values
    df = pd.read_csv("clean.csv")
    df

### check and drop duplicates
    df2=df.drop_duplicates(['SiteID'],keep='first')
    df2

### Check table shape

### df2.shape

### load data into site table

sql = """INSERT INTO site(SiteID,Location, geo_point_2d) VALUES(%s,%s,%s)"""
for row in df2.values.tolist():
    mycursor.execute(sql, tuple(row))
dbconn.commit()

### #load data into readings table

file = open("clean.csv", 'r') 
csv_data = csv.reader(file)
for row in csv_data:
        
                mycursor.execute('INSERT INTO readings(`Date Time`,`NOx`,`NO2`,`NO`,`SiteID`,`PM10`,`NVPM10`,`VPM10`, `NVPM2.5`,\
                            `PM2.5`,`VPM2.5`,`CO`,`O3`,`SO2`,`Temperature`,`RH`,`Air pressure`,`DateStart`,`DateEnd`,\
                            `Current`,`Instrument Type`)'\
                                                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
                                                        row)
            
dbconn.commit()

### populate schema

SchemaT=[['Date Time','Date and time of measurement','datetime'],['NOx','Concentration of oxides of nitrogen','㎍/m3'],['NO2','Concentration of nitrogen dioxide','㎍/m3'],['NO','Concentration of nitric oxide','㎍/m3'],['SiteID','Site ID for the station','integer'],['PM10','Concentration of particulate matter <10 micron diameter','㎍/m3'],['NVPM10','Concentration of non - volatile particulate matter <10 micron diameter','㎍/m3'],['VPM10','Concentration of volatile particulate matter <10 micron diameter','㎍/m3'],['NVPM2.5','Concentration of non volatile particulate matter <2.5 micron diameter','㎍/m3'],['PM2.5','Concentration of particulate matter <2.5 micron diameter    ㎍/m3'],['VPM2.5','Concentration of volatile particulate matter <2.5 micron diameter','㎍/m3'],['CO','Concentration of carbon monoxide','㎎/m3'],

['O3','Concentration of ozone','㎍/m3'],['SO2','Concentration of sulphur dioxide','㎍/m3'],['Temperature','Air temperature','°C'],['RH','Relative Humidity','%'],['Air Pressure','Air Pressure','mbar'],['Location','Text description of location','text'],['geo_point_2d','Latitude and longitude','geo point'],['DateStart','The date monitoring started','datetime'],

['DateEnd','The date monitoring ended','datetime'],['Current','Is the monitor currently operating','text'],['Instrument Type','Classification of the instrument','text']]

SchemaT = pd.DataFrame(SchemaT,columns= ('measure','Desc','Unit'))

SchemaT

### insert into schema
for i, row in SchemaT.iterrows():
    sqlst = """INSERT INTO `schema`(`measure`,`Desc`,`Unit`) VALUES(%s,%s,%s)"""
mycursor.execute(sqlst, tuple(row))

dbconn.commit()

dbconn.close()
