from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://vishnushankar123123:76OZrlPPR60zoop5@cluster0.chjssqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['proj1']
collection = db['proj1-data']

data = list(collection.find())
df = pd.DataFrame(data)

print("✅ Documents fetched:", len(df))
print(df.head())
