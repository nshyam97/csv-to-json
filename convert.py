import pandas as pd
import sys
from collections import OrderedDict
import json


filePath = sys.argv[1]


df = pd.read_csv(str(filePath), dtype={
    "Station": str,
    "Latitude": float,
    "Longitude": float
})

results = []

for (station), bag in df.groupby(["Station"]):
    contents_df = bag.drop(["Station"], axis=1)
    location = [OrderedDict(row) for i, row in contents_df.iterrows()]
    results.append(OrderedDict([("Station", station),
                                ("Location", location)]))
    with open('ExpectedJsonFile.json', 'w') as outfile:
        outfile.write(json.dumps(results, indent=4))

