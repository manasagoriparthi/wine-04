
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
                
Sort and shuffle output -Argentina	12
                         Argentina	15
                         Argentina	25

Reducer Output - Argentina	30.0
                 Australia	36.0
                 Bulgaria	15.0

Chart Type -  For each country, the maximum price of wine is presented as Bar chart

### Manasa Goriparthi
Problem Statement: For each country, find the count of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

Mapper Output - US	235
Spain	110
US	90
US	65
France	66
Spain	73
Spain	65
Spain	110
US	65
US	60
Italy	80
US	48
US	48
France	90
US	185
US	90
US	325
Spain	80
France	290
US	75
US	24
Spain	79
Spain	220
US	60
US	45
New Zealand	57
US	62
US	105
US	60
US	60
Bulgaria	15
US	37
France	22
US	42
Italy	135
France	60
Italy	29
Italy	23
Italy	29
Spain	17
Spain	26
US	55
Italy	39
France	69
Italy	30
Italy	90
US	60
Italy	50
US	40
Italy	100
France	68
France	42
France	28
US	18
US	69
US	25
US	30
Italy	60
Argentina	30
Australia	36
Argentina	25
France	45
Portugal	23
US	36
France	38
US	85
US	50
US	60
US	85
US	45
US	19
Portugal	15
US	54
France	85
US	38
US	28
Italy	75
US	42
Israel	25
Italy	59
Italy	85
Italy	80
France	45
US	22
US	65
US	50
US	10
Portugal	12
Italy	22
US	13
Portugal	10
France	14
US	18
US	36
France	15
France	10
US	24
US	50
Italy	45
US	48
US	20
US	17
US	12
US	10
US	13
US	45
Portugal	12
Argentina	12
US	125
US	25
South Africa	20
Argentina	15
France	20
France	15
Portugal	7
US	59
US	49
US	42
US	93
US	32
US	20
US	100
US	50
Spain	22
Italy	45
Italy	18
US	45
US	26
US	16
US	30
US	42
US	38
US	48
Spain	17
France	18
France	15
US	28
US	25
US	26
US	24
US	55
US	36
Spain	17
US	90

                
Sort and shuffle output -

Reducer Output - 

Chart Type - 

### Nithya Vudayamarri
Problem statement: For each country, find the sum of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

Mapper output - 

Sort and Shuffle output - 

Reducer Output - 

Chart Type - 

### Bhavani Pathuri
Problem statement: For each country, find the average price of wine?

Mapper Input - 0	US	"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."	Martha's Vineyard	96	235	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz

Mapper output - 

Sort and Shuffle output - 

Reducer Output - 

Chart Type - 

## Challenges
- Our dataset has few ASCII values in some of the columns, which caused us some errors while executing the code.
- Some columns had Null values in it, which also caused some issues while executing.
- we also had few challenges using the Github, as the commits and the folders of our team-mates are not showing in the repo, so we have   created another repository. 
- we also had few merge conflicts while pushing the code to the repo.

## Suggestions
- Our suggestions for others who are learning mapreduce is to choose a dataset wisely ,because the dataset with have lots of strings and   null values cause many issues while executing the code. 

## Time Estimates
### Chitralekha
- This assignment took me around 4 hours, getting a correct reducer output for my aggreagate function took a lot of time for me as we     have null values in our dataset. 





