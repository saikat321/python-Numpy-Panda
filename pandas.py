import pandas as pd
import numpy as np

# df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['row1', 'row2 ', 'row3 ', 'row4 ', 'row5 '],
#                   columns=['coloum1', 'coloum2', 'coloum ', 'cloum '])
# print(df)
# print(df.head)
# df.to_csv("test 1")
# accessing the element are two way 1st .loc 2nd .iloc
# print(type(df.loc['row1']))
# print(df.iloc[: ,:])
# #want some specific row
# print(df.iloc[0:3 ,0:2])
#
# #convert data frame to array
# df1 = df.iloc[:,:].shape
# df1 = df.iloc[:,:].values
# print(df1)
#
# #to check if there is any null value
# print(df.isnull().sum())

# to check the frequecy of element
# print(df['coloum ' ].unique())
# print(df['coloum ' ].value_counts())
# print column= enter coloun=mn name in list
# print(df[['coloum1','coloum2']])

df = pd.read_csv('mercedesbenz.csv')
# this separator defines by which the csv file is separated
# df = pd.read_csv('mercedesbenz.csv' ,sep=":")
# print(df.head())
# print(df.info())
# describe it takes out mean median mode etc
# print(df.describe())

# print(df['X0'].value_counts())
# print(df[df['y']>100])


import io as i

# data = ('col1,col2,col3\n'
#         '1,b,1\n'
#         '2,f,2\n'
#         '2,g,3\n')
# print(type(data))
# print(pd.read_csv(i.StringIO(data)))
# df1 =(pd.read_csv(i.StringIO(data), usecols=['col1','col2']))
# print(df1)
# df2 =(pd.read_csv(i.StringIO(data), dtype=object))
# print(df2)
# df3 = df2 =(pd.read_csv(i.StringIO(data), dtype={'col1':int,'col2':str,'col3':float}))
# print(df3)
# #to print a[ particu;ar value
# print((df3['col2'][1]))
# #to get the data type of obj
# print(df3.dtypes)

#
# data = ('index,a,b,c\n'
#         '4,apple,bat,5.6\n'
#         '8,orange,cow,10\n')
# df=pd.read_csv(i.StringIO(data))
# # index co; is used for making it as a row
# df=pd.read_csv(i.StringIO(data),index_col=0)
# print(df)


# data = ('a,b,c\n'
#         '4,apple,bat,5.6\n'
#         '8,orange,cow,10\n')
# df = pd.read_csv(i.StringIO(data),index_col=False)
# print(df)
# df1 = pd.read_csv(i.StringIO(data), usecols=['b','c'],index_col=False)
# print(df1)
#
# # quoting and escape character
# data1= 'a,b\n"hello, \\bob\\, nice tpo see you" ,5'
#
# df2 = pd.read_csv(i.StringIO(data1),escapechar='\\')
# print(df2)


# Pandas to read an json file
# df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data' ,header=None)
# print(df.head())
# df.to_csv('wine.csv')
# # orient records make display of recirds in proper json format...record after records
# print(df.to_json(orient="records"))
# data = '{"employee name":"saikat","email":"saika@sak.fdf" ,"job title":[{"title1":"developer" ,"title2":"testte","title3":"upport"}]}'
# df1 =pd.read_json(data)
# print(df1)


# panda to read HTML
# url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
# url = 'https://en.wikipedia.org/wiki/Mobile_country_code'
# # df = pd.read_html(url ,match='Country' ,header=0)
# df1 = pd.read_html(url )
# print(df1[0])

# read exxel file
# ex = pd.read_excel(r'C:\Users\saikat123\PycharmProjects\funnyProject\P1-OfficeSupplies.xlsx')
# print(ex.head())
#
# # pickle method it is used to coonvert the data structure to disk
# ex1= pd.to_pickle(r'C:\Users\saikat123\PycharmProjects\funnyProject\P1-OfficeSupplies.xlsx')
# ex2 = pd.read_pickle('ex1')
# print(ex2)


df4 = pd.DataFrame(
    {
        "name": ["saikat", "subhash" ,"tukai"],
        "age": [22,34,45],
        "job": ["tester" ,"retired","drveloper"]
    }
)
# print(df4)
# df5 =df4.to_csv('todataframe.csv')
# print(pd.read_csv(i.StringIO('todataframe.csv'),usecols=['name','age'],index_col=False))
print(df4["age"][1])
# print(pd.Series([23,34,56] ,name="ages"))
# df4.to_excel("titan.xlsx",sheet_name="titanic" ,index=False)
# print(pd.read_excel("titan.xlsx" ,sheet_name="titanic"))
#
# print(df4["age"].isin([22]))
# # it will return the number of column and data which is not null
# print(df4["age"].notna())
# print(df4.loc("0"))


pd.read_excel(r'C:\Users\saikat123\PycharmProjects\Data science\mercedesbenz.xlsx' ,sheet_name='mercedesbenz',index_col=0)