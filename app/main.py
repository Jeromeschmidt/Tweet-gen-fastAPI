from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from pydantic import BaseModel, Field
import uvicorn
from datetime import datetime
import random

import os
from dotenv import load_dotenv
from pymongo import MongoClient


from sentence_generator.markov_chain import MarkovChain



app = FastAPI()

load_dotenv()
# client = MongoClient(os.getenv('MONGODB_URL'))
client = MongoClient('mongodb+srv://fastAPITweet:Jms1014neb@cluster0.solua.mongodb.net/mongoDB?retryWrites=true&w=majority')
db = client.get_default_database()
tweet_collection = db.tweet_collection


class TweetModel(BaseModel):
    tweet: str


with open("app/sentence_generator/sherlock.txt",'r') as file:
    text = file.read()
    text = text.split()

markovChain = MarkovChain(text)


@app.get('/')
async def index(response_description="Generates Tweet using Markov chain of random length between 2 and 20"):
    """
    Generates Tweet using Markov chain of random length between 2 and 20
    """
    tweet = markovChain.random_walk(random.randint(2, 20))

    return {"tweet": tweet}


@app.post("/{tweet}", response_description="Add new tweet")
async def favorite_tweet(tweet: str):
    """
    Saves a generated tweet to db
    """
    tweet_dict = {"tweet": tweet, 'created_at': datetime.now(),}
    new_tweet_id = tweet_collection.insert_one(tweet_dict).inserted_id

    return {"tweet": tweet}


@app.get("/tweets", response_description="Get all saved tweets tweet")
async def get_tweets():

    tweets = db["tweet_collection"].find().sort([('created_at', -1)])

    tweets_list = list()

    for elm in tweets:
        tweets_list.append((elm["tweet"], elm["created_at"]))

    return {"tweets": tweets_list}

@app.post('/{tweet_id}/delete', response_description="Delete specific tweet")
def delete_tweet(tweet_id: str):
    """Delete one tweet."""
    db["tweet_collection"].delete_one({'_id': ObjectId(tweet_id)})
    return {"message": "tweet deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
