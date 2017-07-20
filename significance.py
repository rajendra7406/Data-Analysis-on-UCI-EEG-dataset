
import pandas as pd #for dataframe
import numpy as np
import pickle
import matplotlib.pyplot as plt
#Import dict serially from the pickle
with open('readings.pickle', 'rb') as f: 
    dictCount = pickle.load(f)
    alcDictList = pickle.load(f)
    conDictList = pickle.load(f)
    readingsDataframeList = pickle.load(f)

#using one dictionary for simplicity
alcReadingsDict = alcDictList[0]
conReadingsDict = conDictList[0]

#dataframes
alcReadDF = readingsDataframeList[0]
conReadDF = readingsDataframeList[1]

masterdf = pd.concat([alcReadDF,conReadDF], ignore_index=True)
#using groupby 
groupby_category = masterdf.groupby('category')
print(groupby_category.mean())    
groupby_category.boxplot()

#_______histogram plot 
alc = alcReadDF
con = conReadDF
alc.drop(alc.columns[0], axis=1, inplace=True)
con.drop(con.columns[0], axis=1, inplace=True)
alc.hist()
con.hist()
"""
Comparing groups for statistical difference.
Achieved by statistical inference.
Statistical difference means there is statistical evidence that there
is difference. It doesn't tell the nature of difference.

Statistical inference includes :
    Stastical Hypothesis Testing.
Most common way to do statistical inference. 
Always made on null hypothesis.

Null hypothesis has the form:
    "There is no difference among groups" for difference test and
    "There is no association" for correlation tests.
Alternate hypothesis is the contrary of null hypothesis, and never used.
I either reject or accept null hypothesis.

I use significance level, defined as the probability of making a 
decision to to reject null hypothesis.

Steps to apply statistical test:
    1. choose relevant null hypothesis
    2. choose significance level (here 0.05)
    3. Get p value.
    4. if pvalue<significance-level reject null hypothesis
    
Choosing the right statistical test:
    1. Based on type of data:
        quantitative data: discrete, continuous
        or
        qualitative data:binary,nominal,ordinal
        (dataset is continuous data)
    2.  Based on no of samples:
        one sample, two sample, three or more sample
        (I chave two sample data - alcoholics and controlled)
    3. Based on type of data:
        Dependent or independent/paired or unpaired
        (dataset is paired-alcohol and controlled)
        (dataset is independent)
    4. Based on normality of distribution: 
        if its a normal distribution, use parametric test.
        if nature of distribution is not known, use non parametric test.
        to check normality, I use  D’Agostino-Pearson normality test.
    5. One tailed or two tailed tests:
        I choose two tailed test. 
        It is recommended for beginners.
        
"""


#__________significant difference test using 2 sampled t test
from scipy import stats
from scipy.stats import ttest_ind

#function for checking normality for each column
def normalitytest(df):
    count=0
    for column in df:
        if column != 'category':
            tvalue, pvalue = stats.mstats.normaltest(df[column])
            if pvalue<=0.05:
                count=count+1
    return count

print('Performing Normality test')
print('No of electrodes which follow normal distribution')
print('For alcoholics : ',normalitytest(alcReadDF) )            
print('For controlled : ',normalitytest(conReadDF) )            

"""
pvalue < 0.05 satisfies for few electrodes(column)
Not all electrodes(column) follow normal distribution.
So we apply transformation & again check for normality
"""
import math
#performing squaring transformation 
#---------Note: this will take ample amount of time

for column in alcReadDF:
    if column != 'category':
        for index in range(1,257):
            alcReadDF.loc[index,[column]] = math.pow(alcReadDF.loc[index,[column]],2)  

for column in conReadDF:
    if column != 'category':
        for index in range(1,257):
            conReadDF.loc[index,[column]] = math.pow(conReadDF.loc[index,[column]],2)  

#again checking for normality
print('Performing Normality test after transformation')
print('No of electrodes which follow normal distribution')
print('For alcoholics : ',normalitytest(alcReadDF) )            
print('For controlled : ',normalitytest(conReadDF) )            
  
#__the dataframe is now in normal distribution
#___ performing 2 tailed t test
print('elctrodes from both groups which have major significance')
pval= []
tval = []
for column in alcReadDF:
    if column != 'category':
        tvalue, pvalue = ttest_ind(alcReadDF[column], conReadDF[column], equal_var=False)
        pval.append(pvalue)
        tval.append(tvalue)
        if pvalue<=0.05:
            print(column)

#performing prediction------------------------
#random forest classification
mastertemp = masterdf.drop('category',1)
X = mastertemp.iloc[:,:].values
y = masterdf.iloc[:,0].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Fitting the random forest classification to the training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state=0)
classifier.fit(X_train, y_train)

#Predicting the classifier
y_pred = classifier.predict(X_test)

#Producing confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

#the accuracy is 100% . this is overloading
#___________________________________________________________
#dataframe with avg values as rows
lo = ['keys','alcAvg','conAvg']
dff = pd.DataFrame(columns=lo)
for key in alcReadingsDict.keys():
    #converting string values to float values in list
    temp1 = list(map(float, alcReadingsDict[key]))
    temp2 = list(map(float, conReadingsDict[key]))
    #getting mean values
    alcmean = np.mean(temp1)
    conmean = np.mean(temp2)
    #storing reading values to their respective columns 
    dff.loc[key] = [key, alcmean,conmean ]


#bar plot 
#plotting average of each columnn for both alcholics and controlled dataframes
dff.plot(x="keys", y=["alcAvg", "conAvg"], kind='bar')


