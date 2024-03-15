# NOSQL REPORT
The NoSQL tool used for this task is neo4j which is a graph database.  This is a “white board friendly” database. The query language used by neo4j is called Cypher which is an easy graph query language to learn.
The following steps were taken in implementation of this task.

## Data Modelling
 A simple sketch using arrow tools imported from apcjones.com was used in this instance to show a representation of the database, showing entities and relationship. Following the bistol air quality dataset relationship between gases released and sites becomes the important focus of the data model. This will also assist to know when to choose nodes and/or relationships when querying the data.
 
 ![Markdown logo]
 (hhttps://markdown-here.com/img/icon256.png)
 
 
Visualize the schema of the: call db.schema.visualisation()  . This will show the data model as shown below:

![Markdown logo]
 (hhttps://markdown-here.com/img/icon256.png)

 The csv file loaded can also be visualized by calling the function: call db.schema(). This also shows the relationship within th datset.

![Markdown logo]
 (hhttps://markdown-here.com/img/icon256.png)

NoSQL database Implementation using neo4j for the Bristol air quality data
Making use of the desktop version of neo4j, the following Cypher queries were implemented.
## Load CSV file
##### Query:
_LOAD CSV WITH HEADERS FROM_
_‘file:/// C:/Users/offor/OneDrive/Desktop/clean.csv’ AS line_
_WITH line_
_LIMIT 1_
_RETURN line_

_The above query returns:_
_{_
  _"identity": 3,_
  _"labels": [_
    _"Site"_
  _],_
  _"properties": {_
_"siteID": 452_
  _}_
}_
The above query also enables us to have a sneak peak into the structure of the dataset.
•	The node and relationship syntax were determined. The relationship was simulated with one SiteID 452. This was created with the following syntax:

_create (a)-[:READING_DATE_TIME]->(c1)_
_create (a1)-[:READING_DATE_TIME]->(c2)_
_create (a2)-[:READING_DATE_TIME]->(c3)_

_create (c1)-[:RELEASED_AMOUNT]->(f1)_
_create (c2)-[:RELEASED_AMOUNT]->(f2)_
_create (c3)-[:RELEASED_AMOUNT]->(f3)_

Executing Cypher query *call.db.index* that shows the list of all indexes that has been created in the database.


![Markdown logo]
 (hhttps://markdown-here.com/img/icon256.png)
 


##### CYPHER MAIN LOAD
The ‘merge’ Cypher query connects relationships with nodes through the ‘parent’ and ‘child’ system. Also a new node if required is added.  

_LOAD CSV WITH HEADERS FROM_
‘_file:/// C:/Users/offor/OneDrive/Desktop/clean.csv’ AS line_
_WITH line_
_LIMIT 1_
_RETURN line_

_merge (a:Gas {gas: "NOx"})_
_merge (a1:Gas {gas: "NO2"})_
_merge (a2:Gas {gas: "NO"})_

_merge (b:Site {siteID: 452})_

_merge (b)-[:GAS]->(a)_
_merge (b)-[:GAS]->(a1)_
_merge (b)-[:GAS]->(a2)_
_create (c1:ReadingDateTime {dateTime: "2014-08-22T08:00:00+00:00"})_
_create (c2:ReadingDateTime {dateTime: "2014-08-22T08:00:00+00:00"})_
_create (c3:ReadingDateTime {dateTime: "2014-08-22T08:00:00+00:00"})_

_create (f1:ReleasedAmount {name: "PM10", value:"8.7"})_
_create (f2:ReleasedAmount {name: "NVPM10", value:"6.8"} )_
_create (f3:ReleasedAmount {name: "VPM10", value:"1.9"})_

#### BASIC ANALYSIS OF GRAPH
The Cypher query for the graph is: MATCH P=()- RETURN P LIMIT 25. Due to the flexibility 
of neo4j, it is possible to focus and gain insight on a specific node and its relationships. 
The syntax to analyze the graph is :
 match(n) RETUN n limit 14. This produces the graph below:
 
 
 ![Markdown logo]
 (hhttps://markdown-here.com/img/icon256.png)
 

 
As can be seen in the graph nodes and relationships shown in the graph determines the connection between nodes as well as to the red node which is the site. New nodes can be generated using the create statement and this is one of the good uses of a graph database due to its flexibility. 
##### Indexes and Constraints in Graph Databases
Creating indexes is the first step towards structuring a database. Constraints are added to the indexes which is very import in preventing repetition of a node.
In conclusion, despite the powerful ability of neo4j to produce and graph relationship it may not be suitable to every type of domain problem that a graph query will solve. If I should do this task again I would prefer to use othe NOSQL databases.

##### References list:  
* Neo4j Workshop: Importing CSV data(14 April 2021) Available at April :
https://www.youtube.com/watch?v=Krn2yyUDhUA&t=768s)   (Accessed: 21 April 2022)

* Robinson, I. et al. (2015). Graph Databases. Sebastopol, CA: O’Reilly pp. 25-30.