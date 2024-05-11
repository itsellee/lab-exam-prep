import pandas as pd
import numpy as np
Table = pd.read_csv("ExamTable.csv")
Table = Table.dropna()
NewTable = pd.DataFrame()
NewTable = pd.concat([NewTable, Table.loc[Table['Interval']=="30-0"]], ignore_index=True)
NewTable.to_csv('b1_output1.csv')


# Read table 1 and then export it to create a table 1 copy 
# Iupytmportant command data.loc that will locate the id's; will also be used for filtering and have a copy of the data frame
# Pandas match; pandas api reference 
# More on .csv manipulation (ex. transposition of the first 5 columns, or the first 2-th columns lang)
