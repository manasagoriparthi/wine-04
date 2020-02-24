
# wine-reviews-04

## BigData 44517 Sec01-04

## Team Members
- Bhavani Pathuri - s534867@nwmissouri.edu
- Chitralekha Chikku - s534630@nwmissouri.edu
- Nithya Vudayamarri - s534641@nwmissouri.edu
- Manasa Goriparthi - s534782@nwmissouri.edu

## Links
- [Repository Link](https://github.com/manasagoriparthi/wine-04)
- [Issuetracker Link](https://github.com/pathuribhavani/wine-reviews-04/issues)

## Introduction
- The wine review Dataset has 130K wine reviews with variety, location, winery, price, and description. The source of this dataset is by Zackthoutt (where his idea was by a documentary on master sommeliers). This Dataset offers some great oppurtunities for sentimental analysis and other text related predictive models.

## Data Source
- VOLUME: The size of data set is 174 MB and it has 14 columns and many rows. The source of this data set is by Zackthoutt (where his idea was by a documentary on master sommeliers.)

- VARIETY: This is a structured data set available in CSV format and JSON format.

- VELOCITY: The dataset is last updated 2 years ago, as there are no columns added recently the velocity of the data set is zero

- VERACITY: The Data set is pretty clean and not messy. The data seems to be trustworthy. The quality and accuracy of the data is quite up to the mark.

- VALUE: This dataset offers some incredible opportunities for assumption examination and other content related prescient models. The general objective is to make a model that can recognize the assortment, winery, and area of a wine dependent on a portrayal.

## Link for the datasource
https://www.kaggle.com/zynicide/wine-reviews

## Big Data Problems
### Chitralekha chikku
Problem Statement: For each country, find the maximum price of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

Mapper Output - US	235
                Spain	110
                US	90
![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/chitra_images/chitra_mapperoutput%20.png)

Sort and shuffle output -Argentina	12
                         Argentina	15
                         Argentina	25

![SortShuffle Output](https://github.com/manasagoriparthi/wine-04/blob/master/chitra_images/chitra_sortandshuffleoutput.png)

Reducer Output - Argentina	30.0
                 Australia	36.0
                 Bulgaria	15.0
![Reducer Output](https://github.com/manasagoriparthi/wine-04/blob/master/chitra_images/chitra_reduceroutput.png)

Chart Type -  For each country, the maximum price of wine is presented as Bar chart
![Graphical Representation](https://github.com/manasagoriparthi/wine-04/blob/master/chitra_images/chitra_chart.png)

### Manasa Goriparthi
Problem Statement: For each country, find the count of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

Mapper Output - US	235
Spain	110
US	90

![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/manasa_images/manasa-mapper%20output.png)

Sort and shuffle output -Argentina	12
Argentina	15
Argentina	25

![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/manasa-sortandshuffle-output.png)

Reducer Output - Argentina	82.0
Australia	36.0
Bulgaria	15.0

![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/manasa-reduceroutput.png)

Chart Type - For each country, the count price of wine is presented as line graph.

![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/manasa-line-graph.png)

### Nithya Vudayamarri
Problem statement: For each country, find the sum of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

### Mapper output  
![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/Nithya_MapperOutput.png)


### Sort and Shuffle output 
![SortShuffle Output](https://github.com/manasagoriparthi/wine-04/blob/master/Nithya_SortShuffleOutput.png)

### Reducer Output - 
![Reducer Output](https://github.com/manasagoriparthi/wine-04/blob/master/Nithya_Reduceroutput.png)

### Chart Type - 
![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/Nithya_Graph.png)

### Bhavani Pathuri
Problem statement: For each country, find the average price of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

### Mapper output 
![Mapper Output](https://github.com/manasagoriparthi/wine-04/blob/master/MapperOutput.png)

### Sort and Shuffle output 
![SortShuffle Output](https://github.com/manasagoriparthi/wine-04/blob/master/SortShuffleOutput.png)

### Reducer Output 
![Reducer Output](https://github.com/manasagoriparthi/wine-04/blob/master/ReducerOutput.png)

### Chart Type 
![Graphical Representation](https://github.com/manasagoriparthi/wine-04/blob/master/BhavaniPathuri/Graph.png)

## Challenges
- Our dataset has few ASCII values in some of the columns, which caused us some errors while executing the code.
- Some columns had Null values in it, which also caused some issues while executing.
- we also had few challenges using the Github, as the commits and the folders of our team-mates were not reflecting the repo, so we have   created another repository. 
- we also had few merge conflicts while pushing the code to the repo.

## Suggestions
- Our suggestions for others who are learning mapreduce is to choose a dataset wisely, because the dataset with lots of strings and   null values cause many issues while executing the code.

## Time Estimates
### Chitralekha
- This assignment took me around 4 hours, getting a correct reducer output for my aggreagate function took a lot of time for me as we     have null values in our dataset.
### Bhavani Pathuri
- This assignment took me around 5-6 hours because of the issues of my github where i did all my commits and pushed the code but it didn't reflect in the repository and getting correct out for my average function as our data set contains lots of null and ASCII values.
### Nithya Vudayamarri
- This assignment took e around 3-4 hours because the first repo link in the github did not refelect many of our commits. So we group members created a new one and started the process again and solved the mistake. I solved sum function, which took me around 40 minutes to do and take all the sceenshots.





