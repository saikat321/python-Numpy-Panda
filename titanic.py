import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.axes._base import _axis_method_wrapper

train = pd.read_csv(r'D:\Busines analyst\Python hands on\EDA1-master\titanic_train.csv')
# print(train)
# checking missing data
# print(train.isnull())

# we cant check many data using is null so we will use heatmap from seaborn yo analyze missing data
# coloumn on which byellow color is present are the null value
# sns.heatmap(train.isnull(),yticklabels=False ,cbar=False,cmap='viridis')
# plt.show()
# we will check sme more data check on how many people survived
# sns.set_style('whitegrid')
# sns.countplot(x='Survived' ,data=train)
# plt.show()

# we are checking now different data
# bases on this survived we will seggregate more on male n female
# sns.set_style('whitegrid')
# sns.countplot(x='Survived' ,hue='Sex' ,data=train ,palette='RdBu_r')
# plt.show()

# bases on this survived we will seggregate more on Pclass
# sns.set_style('whitegrid')
# sns.countplot(x='Survived' ,hue='Pclass' ,data=train ,palette='rainbow')
# plt.show()

# # now we will take distplot to check the age distributionn
# sns.displot(train['Age'].dropna() ,kde=False ,color='darkred' ,bins=40)
# plt.show()

# now we will take hist to check the age distributionn
# sns.histplot(train['Age'] ,color='Darkred')
# plt.show()
# train['Age'].hist(bins=30 ,color='darkred' ,alpha=0.3)
# plt.show()

# now we will take a countplot for how many sibling and spouse
# sns.countplot(x='SibSp' ,data=train)
# plt.show()

# # train fare histogram
# train["Fare"].hist(bins=40 ,color='green',figsize=(8,4))
# plt.show()



# we will remove the null value  DATA CLEANING PART
# as we know that age is somewahta related to pclass so we will check that by checking average value
# plt.figure(figsize=(12,7))
# sns.boxplot(x='Pclass' ,y='Age' ,data=train ,palette='winter')
# plt.show()
# from above this we got yhe average age that is present in all the 3 clas
# so we will write a function whwre we will return all the age and we will check which is not null
# here we are taking an average value of all pclass passenger and assigning that average value to aal the missing age
def input_age(cols):
    Age =cols[0]
    Pclass =cols[1]
    if pd.isnull(Age):
        if Pclass ==1:
            return 37
        if Pclass ==2:
            return 29
        else:
            return 24
    else:
        return Age
# now apply this function to check the age and pclass
train['Age']=train[['Age' ,'Pclass']].apply(input_age,axis=1)
# we can see that missing data in  age has gone
# sns.heatmap(train.isnull(),yticklabels=False ,cmap='viridis' ,cbar=False)
# plt.show()

# cur4ently there is a lot of empty cell in cabin so we  need to do FEATURE ENGINEERING
# hence for now we will drop it =coloumn
train.drop('Cabin',axis=1 ,inplace=True)
# train.head()

# Now to check the model we need to convert the categorical data to numeric
# so we will check the categorical data and convert them in numeric
sex = pd.get_dummies(train['Sex'] ,drop_first=True).head()
Embarked = pd.get_dummies(train['Embarked'] ,drop_first=True).head()
# print(Embarked.head())
#    Q  S
# 0  0  1
# 1  0  0
# 2  0  1
# 3  0  1
# 4  0  1
# above there are 3 category  P Q S WHERE s is 0,1   Q is 1,0   and since we dropped 1st coloumn so P is 0,0

# Now we will drop all coloumn that are not neccesary
train.drop(['Age','Sex',"Embarked",'Ticket'],axis=1 ,inplace=True)
print(train.head())

# since we have chenged the categorical  feature so now we need to concat it with main data
train =pd.concat([train,sex,Embarked],axis=1)
# print(train.head())

# now we will built a Logistic regressin model where we first need to difference UNIVARIATE AND BIVARIATE
# mean we need to diff dependent and independent
# here survived is a dependent we will drop it and create a TRAINING DATA SET
# Train Test Split

train.drop('Survived' ,axis=1)
# our output data set
print(train['Survived'].head())

# now we will do Train test split
import sklearn_model as sk
X_train ,X_test ,Y_train ,Y_test = sk.train_test_split(train.drop('Survived',axis=1),train['Survived'],test_size=0.30,random_state=101)