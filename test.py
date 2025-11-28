test = {"Name": ["Anna", "Darya", "Boris", "Yana"], "id": [1, 2, 6, 0]}
import pandas as pd
df = pd.DataFrame(test)
#print(df)


print(df.nsmallest(3, "id"))