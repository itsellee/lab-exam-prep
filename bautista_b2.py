import pandas as pd
import numpy as np
Table = pd.read_csv("ExamTable.csv")
Table = Table.dropna()
NewTable = pd.DataFrame()
NewTable = pd.concat([NewTable, Table.loc[Table['Genus'].str.startswith('St' or 'st')]])
NewTable.to_csv('b2_output1.csv')