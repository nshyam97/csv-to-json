import pandas as pd
import sys


filePath = sys.argv[1]


df = pd.read_csv(str(filePath))

df.to_json('data.json')
