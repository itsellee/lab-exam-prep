import pandas as pd 
Table=pd.read_csv('ExamTable.csv') 
Table=Table.dropna() 

FiveColumn=Table.loc[:, :"Depth (m)"]
NewTable=FiveColumn.transpose()
NewTable.to_csv("fivecolumn1.csv", index=False)

