"""1st to make sure emdeddings works."""

from dotenv import load_dotenv
import os
import basilica
from scipy import spatial

load_dotenv()

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=abc321

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")


def basilica_connection():
    connection = basilica.Connection(BASILICA_API_KEY)
    print(connection)
    return connection


if __name__ == "__main__":
    sentences = [
        "This is a sentence",
        "This is a similar sentence",
        "I don't think this sentence is very similar at all..."
        ]

    connection = basilica_connection()

    embeddings = list(connection.embed_sentences(sentences))

    for emb in embeddings:
        print(type(emb))  # > list
        print(len(emb))  # > 768
        print(emb)
        print("---------------")

    result = connection.embed_sentence("Hello World", model="twitter")
    print(type(result))  # > list
    print(len(result))  # > 768
    print(result)

    print(spatial.distance.cosine(embeddings[0], embeddings[1]))
    print(spatial.distance.cosine(embeddings[0], embeddings[2]))
