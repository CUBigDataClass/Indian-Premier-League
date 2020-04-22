# Indian-Premier-League
This project aims to show some cool intresting facts, records, results of IPL



## Team Meambers: <br/>
#### Nithin Veer Reddy<br/>
#### Abhinivesh Palusa<br/>
#### Lokin Sai Makkenna<br/>
#### Mohan Dwarampudi<br/>

### Extract

1.  Data has been sourced from multiple areas -
    -   Scrapping from popular cricketing websites.
    -   Scrapping wiki pages.
    -   Through Google API for Geo points.
    -   Kaggle datasets.
    
2.  All the data is then stored in Amazon S3, which is then pushed into DynamoDB. S3 event invokes AWS Lambda which does the    data parsing before it is rested in DynamoDB.  

3.  The entire data has been utilized into three tables in DynamoDB, namely - deliveries, matches, players. This data acts as a source of truth for all the further operations.

