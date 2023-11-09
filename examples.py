import pandas as pd
import numpy as np

data = {
    'Name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'Age': [42, 52, 36, 24, 73],
    'Maths': [4, 24, 31, 2, 3],
    'English': [25, 94, 57, 62, 70]
}


# data frame
df = pd.DataFrame(data)
print(df.head(2))
# print(df.tail(2)) - end of data to print
# print(df.describe()) - summary of data
# 
# print(df['Name']) - print column

#num py arrays
np_array = df[['Name', 'Age']].to_numpy()
mean_scores = np.mean(np_array, axis=0)

print(mean_scores)
print(np_array)





