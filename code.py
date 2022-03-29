import pandas as pd
import plotly.figure_factory as fd0

df = pd.read_csv('E:/PYTHON__/C108/data.csv')
hei = df['Height(Inches)'].tolist()

gr = fd0.create_distplot([hei],['Height Avg h bhai'],show_hist=False)
gr.show()