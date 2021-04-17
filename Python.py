import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("cups of coffee vs hours of sleep.csv")
fig = px.line(df, x = "Coffee in ml", y = "sleep in hours")
fig.show()