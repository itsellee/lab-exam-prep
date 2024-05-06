import pandas as pd
import numpy as np
Table = pd.read_csv("ExamTable.csv")
uniqspecies = (Table['Scientific Name'].unique())

NewTable = pd.DataFrame()
NewTable['Scientific Name']= uniqspecies

AveSize = []
for i in range(len(uniqspecies)): 
    AveSize.append((Table.loc[Table['Scientific Name']== uniqspecies[i], ['Size Est (cm)']].mean().values[0]))
NewTable['Average Size Est (cm)'] = AveSize
NewTable.to_csv('b4_output1.csv')
