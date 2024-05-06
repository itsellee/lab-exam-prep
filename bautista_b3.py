import pandas as pd
import numpy as np
Table = pd.read_csv("ExamTable.csv")
listofspecies = (Table['Scientific Name'])
uniqspecies = pd.unique(listofspecies)
pd.DataFrame(uniqspecies, columns = ['Scientific Name']).to_csv('b3_output1.csv')