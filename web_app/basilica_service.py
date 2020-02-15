"""1st to make sure emdeddings works."""

from dotenv import load_dotenv
import os
import basilica
from scipy import spatial

load_dotenv()

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=abc321

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

sentences = [
    "This is a sentence",
    "This is a similar sentence",
    "I don't think this sentence is very similar at all..."
]
with basilica.Connection('5b537344-60f8-fc07-1981-05f54ea445b4') as c:
    embeddings = list(c.embed_sentences((sentences)))

print(list(embeddings))

print(spatial.distance.cosine(embeddings[0], embeddings[1]))
print(spatial.distance.cosine(embeddings[0], embeddings[2]))

for emb in embeddings:
    print(type(emb))
    print(emb)
    print("---------------")
