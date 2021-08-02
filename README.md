# Sherlock Tweet Generator:

## Tech Stack
- Python
- FastAPI
- MongoDB
- Docker
- Heroku

[Heroku](https://sherlock-tweetgen-fastapi.herokuapp.com/)
[Docs](https://sherlock-tweetgen-fastapi.herokuapp.com/docs)
[Github](https://github.com/Jeromeschmidt/Tweet-gen-fastAPI)

## Tweet Generation:
Tweets are generated using a Markov chain to build a word map of Sherlock Holmes text. It then performs a random walk to create sentences starting with start words and ending with stop words and punctuations.


## Endpoints:
| Route | Method | Description |
| ----------- | ----------- | ----------- |
|/ |GET | Generates and returns a tweet |
|/{tweet}| POST | Saves a generated tweet |
|/ |GET | Gets a list of all saved tweets |
|//{tweet_id}/delete | POST | Deletes a tweet |


## 🚀 Getting Started

## Prerequisites
* python3.7

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
python3 app/trade.py
```


## TODO:
- Build and connect Frontend
- Implement Pydantic Types

## Resources:
https://fastapi.tiangolo.com/
https://medium.com/analytics-vidhya/dockerize-your-python-flask-application-and-deploy-it-onto-heroku-650b7a605cc9
https://docs.docker.com/
https://devcenter.heroku.com/
