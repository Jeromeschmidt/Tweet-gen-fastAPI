# Sherlock Tweet Generator:

## Tech Stack
- Python
- FastAPI
- MongoDB Atlas
- Docker
- Heroku
- Pytest

[Heroku](http://sherlock-tweetgen-fastapi.herokuapp.com/tweets/)

[Docs](https://sherlock-tweetgen-fastapi.herokuapp.com/docs)

[Github](https://github.com/Jeromeschmidt/Tweet-gen-fastAPI)

## Tweet Generation:
Tweets are generated using a Markov chain to build a word map of Sherlock Holmes text. It then performs a random walk to create sentences starting with start words and ending with stop words and punctuations.

## API


### Endpoints:
| Route | Method | Description |
| ----------- | ----------- | ----------- |
|/ |GET | Returns an index page |
|/tweets/ |GET | Generates and returns a tweet |
|/tweets/{tweet_id}  |GET | Returns a specific tweet |
|/tweets/{tweet}| POST | Saves a generated tweet |
|/tweets/all |GET | Gets a list of all saved tweets |
|/tweets/{tweet_id} | DELETE | Deletes a tweet |

### Examples Responses:

/tweets/ | GET

![/tweets/ | GET](/assets/images/tweet.png)


/tweets/{tweet_id} | GET

![/tweets/{tweet_id} | GET](/assets/images/retrieve_tweet.png)


/tweets/{tweet} | POST

![/tweets/{tweet} | POST](/assets/images/favorite_tweet.png)


/tweets/all | GET

![/tweets/all | GET](/assets/images/get_all_tweets.png)


/tweets/{tweet_id} | DELETE | Success

![/tweets/{tweet_id} | DELETE | success](/assets/images/delete_tweet_success.png)


/tweets/{tweet_id} | DELETE | Failure

![/tweets/{tweet_id} | DELETE | success](/assets/images/delete_tweet_failure.png)



## 💻 Local Development

```bash
# clone the repo
git clone https://github.com/Jeromeschmidt/Tweet-gen-fastAPI
```
```bash
# cd into the repo
cd Tweet-gen-fastAPI
```
```bash
# create a virtual environment
python3.7 -m venv venv
```
```bash
# Activate virtual environment
source venv/bin/activate
```
```bash
# Install the requirements
pip3 install -r requirements.txt
```
```bash
# run the program
python3 app/main.py
```

### Test
```bash
# run Pytest
cd app
python3 -m pytest -s tests
```


## TODO:
- Build and connect Frontend
- Add CI

## Resources:
https://fastapi.tiangolo.com/

https://medium.com/analytics-vidhya/dockerize-your-python-flask-application-and-deploy-it-onto-heroku-650b7a605cc9

https://docs.docker.com/

https://devcenter.heroku.com/

https://ycd.github.io/manage-fastapi/
