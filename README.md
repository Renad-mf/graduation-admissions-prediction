# graduation-admissions-prediction

***Introduction***

Am I going to enter my dream university?
every student wishes to enter their desired university, but unfortunately, not
all of them get accepted because acceptance depends on many criteria like
GRE Score, TOEFL Score , graduate GPA, Letter of Recommendation,
Research Experience and many more it depends on the university your
applied to it, therefore it will be very helpful for the high school students if
there is a way to predict whether they will be accepted so they can improve
themselves before it is too late .

***Aim of this project***

In this project, we visualize the variables of the graduation admission
dataset and see the relationship between the variables with the target
feature “chance of admit”, we implemented two prediction models and
compare their performance using the accuracy equation.

***Problem Description***

We went to predict student chance of admissions into their desired university

***The dataset contains many features which are important to get accepted into
university include:***

• Graduate Record Scores ( out of 340 )

• TOEFL Scores ( out of 120 )

• Undergraduate GPA ( out of 10 )

• Research Experience ( yes=1,no=0 )

• Chance of Admit ( ranging from 0 to 1 )

***from the heatmap, the CGPA is the most correlated
variable with the Chance of Admit. so, we decided to perform simple linear
regression using CGPA as our input variable.***

***Experimental Results :***

to improve the model performance, we tried a different model called Logistic
regression

***Analyze :***

After brief understanding of dataset, we wanted to know what is the most
influential feature on our target feature and to do so we use heat map .

As it is shown on the heat map the CGPA is the influential feature so we
decided to make it our input variable.

After we upload the libraries and our dataset we check for missing values
and we found none ,then before starting implement simple linear regression
we dropped the data that we don’t need in our model and then visualize the
correlated features .

We started to apply a simple linear regression implementation on our data(
the chance of admit as our dependent variable(y) and CGPA as the
independent variable (x) )by splitting data into training and testing ,then we
modeled the data in the Linear Regression model ,after that we trained and
test our model using .fit( ) and .predict( ) respectively ,finally we evaluated
the model performance by using 4 evaluation matrices which are: Mean
Absolute Error(MAE) ,Mean Square Error(MSE),Root Mean Square
Error(RMSE) and R Square , then we get accuracy of our model using
.score( ) and get 72.7% accuracy .

***Our improvement and implementation :***

We wanted a way to improve our model performance, so we decided to try
different models . we chose to try Logistic regression to classify whether
student will be accepted or rejected .
First, we lode the libraries and data and select “chance of admit” as our
dependent variable(y) and “CGPA” as the independent variable (x) and
drop other columns then we split the data into training and testing and by
using .fit( ) and .predict( ) we trained and test our model finally we get
accuracy to see if the model has improved than our linear model
performance or not.

The accuracy was 77.8% ,it improves 5% then linear model performance

***Conclusion***

After implementing different models to our data, we conclude that the
logistic regression model gives 77.8% accuracy and linear regression gives
72.7% accuracy , logistic regression performs better prediction .
The prediction of this dataset performs better when we use classification
prediction implemented in logistic regression model.

