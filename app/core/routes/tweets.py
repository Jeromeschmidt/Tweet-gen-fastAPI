from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from core.sentence_generator.build_chain import build_markov_chain
import random
from datetime import datetime

markov_chain = build_markov_chain()

from core.database.db import (
    add_tweet,
    delete_tweet,
    retrieve_tweet,
    retrieve_tweets,
)
from core.models.tweet import (
    ErrorResponseModel,
    ResponseModel,
    TweetSchema,
)

router = APIRouter()

@router.get('/')
async def index(response_description="Generates Tweet using Markov chain of random length between 2 and 20"):
    """
    Generates Tweet using Markov chain of random length between 2 and 20
    """
    tweet = markov_chain.random_walk(random.randint(2, 20))

    return {"tweet": tweet}


@router.post("/{tweet}", response_description="Add new tweet")
async def favorite_tweet(tweet: str):
    tweet = {"tweet": tweet, 'created_at': datetime.now()}
    tweet = jsonable_encoder(tweet)
    new_tweet = await add_tweet(tweet)
    return ResponseModel(new_tweet, "Tweet added successfully.")


@router.get("/all", response_description="Get all saved tweets tweet")
async def get_tweets():
    tweets_list = await retrieve_tweets()
    return {"tweets": tweets_list}


@router.get("/{tweet_id}", response_description="Get one saved tweet")
async def get_tweet(tweet_id: str):
    tweet = await retrieve_tweet(tweet_id)
    return {"tweet": tweet}


@router.delete('/{tweet_id}', response_description="Delete specific tweet")
async def remove_tweet(tweet_id: str):
    """Delete one tweet."""
    deleted_tweet = await delete_tweet(tweet_id)
    if deleted_tweet:
        return ResponseModel(
            "Tweet with ID: {} removed".format(tweet_id), "Tweet deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Tweet with id {0} doesn't exist".format(tweet_id)
    )
