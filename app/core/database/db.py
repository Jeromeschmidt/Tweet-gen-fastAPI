import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.mongoDB

tweet_coll = database.get_collection("tweet_collection")


# helpers

def tweet_helper(tweet) -> dict:
    return {
        "_id": str(tweet["_id"]),
        "tweet": tweet["tweet"],
        "created_at": tweet["created_at"],
    }


# Retrieve all tweets present in the database
async def retrieve_tweets():
    tweets = []
    async for tweet in tweet_coll.find():
        tweets.append(tweet_helper(tweet))
    return tweets


# Add a new tweet into to the database
async def add_tweet(tweet_data: dict) -> dict:
    new_tweet = await tweet_coll.insert_one(tweet_data)
    return tweet_helper(tweet_data)


# Retrieve a tweet with a matching ID
async def retrieve_tweet(id: str) -> dict:
    tweet = await tweet_coll.find_one({"_id": ObjectId(id)})
    if tweet:
        return tweet_helper(tweet)

# Delete a tweet from the database
async def delete_tweet(id: str):
    tweet = await tweet_coll.find_one({"_id": ObjectId(id)})
    if tweet:
        await tweet_coll.delete_one({"_id": ObjectId(id)})
        return True
    return False

# Update a tweet with a matching ID
async def update_tweet(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    tweet = await tweet_coll.find_one({"_id": ObjectId(id)})
    if tweet:
        updated_tweet = await tweet_coll.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_tweet:
            return True
        return False
