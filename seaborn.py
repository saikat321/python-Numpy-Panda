import  seaborn as sns
import  matplotlib.pyplot as plt
df = sns.load_dataset('tips')
# print(df.head())
# print(df.corr())
# print(df.dtypes)
# sns.heatmap(df.corr())
# print(sns.jointplot(x ='tip' , y= 'total_bill' ,data=df ,kind='reg'))
# sns.pairplot(df)
# we can also make the scatter plot on some particular coloumn that is pesent
# sns.pairplot(df ,hue='day' )
# plt.show()

# if we need to  find out soe count
# print(df['smoker'].value_counts())
# dist plot it give a discrete form of a particular coloumn aur data
# sns.displot(df['tip'])
# # kde basically draw  curve kde = kernel density estimation
# sns.displot(df['tip'] ,kde= True ,bins=10)
# plt.show()





# # categorical feature plot
# sns.countplot(y='day' ,data=df)
# plt.show()
# diff betwween bar plot and countlot is on bar pot we need  to give both axis while in countplot we dont need that
# sns.barplot(x='tip' ,y='sex' ,data=df)
# plt.show()

# box pot
# sns.boxplot('day' ,'total_bill' ,data=df ,palette='rainbow')
# plt.show()

# box plot also not take the categorical feature
# orient mean if u want to inculde all the feature
# sns.boxplot(data=df ,orient='v')
# plt.show()

# # hue mean we are advicing to classify the wrt the givenhue feature
# sns.boxplot('total_bill' ,'day' ,hue='smoker' ,data=df)
# plt.show()

# # violin plot heps us to see the distribution wrt to KDE and box pot it comprises both
# sns.violinplot(x='total_bill' ,y='day' ,data=df ,palette='rainbow')
# plt.show()

# load iris data set and prac
iris = sns.load_dataset('iris')
print(iris.head)
sns.lineplot(data=iris)
plt.show()

