from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sentence_generator.markov_chain import MarkovChain

import random



app = FastAPI()

templates = Jinja2Templates(directory="templates")



with open("sentence_generator/sherlock.txt",'r') as file:
    text = file.read()
    text = text.split()

markovChain = MarkovChain(text)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    sentence = markovChain.random_walk(random.randint(2, 20))

    # return {"message": sentence}
    return templates.TemplateResponse("index.html", {"request": request, "sentence": sentence})



@app.get('/view_favorites')
def view_favorites():
    # return render_template('view_favorites.html', tweets=tweet_coll.find().sort([('created_at', -1)]))
    return {"message": "Favorites"}

@app.get('/description')
def description():
    # return render_template('description.html')
    return {"message": "description"}
