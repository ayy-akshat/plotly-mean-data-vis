import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
means = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

# print(df)
print(means)

d = px.scatter(means, x="student_id", y="level", size="attempt", color="attempt")
d.show()