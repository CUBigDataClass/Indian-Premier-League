# Indian-Premier-League
This project aims to show some cool intresting facts, records, results of IPL



## Team Meambers: <br/>
#### Nithin Veer Reddy<br/>
#### Abhinivesh Palusa<br/>
#### Lokin Sai Makkenna<br/>
#### Mohan Dwarampudi<br/>

### Extract

-   Data has been sourced from multiple areas -
    -   Scrapping from popular cricketing websites.
    -   Scrapping wiki pages.
    -   Through Google API for Geo points.
    -   Kaggle datasets.
-   All the data is then stored in Amazon S3, which is then pushed into DynamoDB. S3 event invokes AWS Lambda which does the    data parsing before it is rested in DynamoDB.  
-   The entire data has been utilized into three tables in DynamoDB, namely - deliveries, matches, players. This data acts as a source of truth for all the further operations.

### Transform

-   All the semi-parsed data is transformed into a meaningful entry - JSON.  
-   Triggers on DynamoDB would invoke AWS Lambda whenever a new entry is added into DynamoDB. 
-   AWS Lambda transforms the data into meaningful patterns, which are further loaded into ElasticSearch cluster.
-   AWS Lambda also fetches additional Geo data through Google API.
-   AWS Lambda uses Redis for a quick Key: Value mapping lookup.

### Load

-   ElasticSearch indices all the incoming data from Lambdas.
-   Data on ElasticSearch is split on the nodes in the cluster.
-   All the 3 formats of the data are stored in different indices -
    -   deliveries
    -   matches
    -   players


### ElasticSearch

-   A two node cluster, served out via Load Balancer.
-   Load Balancer endpoint would be the face of the ElasticSearch.
-   There are separate indices for all three types of data sources which are mentioned before.


### Kibana

-   This is the face of our project.
-   Dashboards are generated separately for each index.
-   Visualizations such as Geo-tagging, Heatmaps, Custom Metrics, Pie Charts, Bar Graphs, Line Plots, etc. are integrated.
-   Filters applied on a visualization is applied across the dashboard.
-   Dashboard URLs:
    -   deliveries: http://bdaipl.tech/goto/5cfc0ec8469aa162cac5bd4e332e9e73
    -   matches:    http://bdaipl.tech/goto/46fd3de9a53d6303bd0df15d80b3353d
    -   players:    http://bdaipl.tech/goto/bd0aa593d7fa7f6fda73fdd36745ba9c
    
    
### NGINX

-   Utilized for the purpose of port forwarding.
-   It forwards the request received on 80 to the Kibana's listening port, making Kibana as the face of the application.


### URL for our project:    http://bdaipl.tech/
