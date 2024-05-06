import pandas as pd
import numpy as np
Table = pd.read_csv("ExamTable.csv")
Table = Table.dropna()
NewTable = pd.DataFrame()
NewTable = pd.concat([NewTable, Table.loc[Table['Interval']=="30-0"]], ignore_index=True)
NewTable.to_csv('b1_output1.csv')

