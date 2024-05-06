import pandas as pd
import numpy as np
Table = pd.read_csv("ExamTable.csv")
sciname = Table.loc[Table['Scientific Name']=='Pomacentrus adelus']
count = sciname['Count']
sum =0
for i in count:
    sum = sum+i
average = sum/len(count)
print("The average count for Pomacentrus adelus is:", average)

# The output for the average count for Pomacntrus adelus is 1.5833333333333333
