import pandas as pd
import lxml


url = 'https://pt.wikipedia.org/wiki/Big_Brother_Brasil_1'

dfs = pd.read_html(url) #dfs = pd.read_html(url, match='Origem')

print(type(dfs))
print(len(dfs))
print(dfs)