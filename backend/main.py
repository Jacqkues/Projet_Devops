from fastapi import FastAPI, Request, Form , APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
import pandas as pd
from data.generator import *

from api_spotify.api import *
import csv
from pymongo import MongoClient
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from requests import post, get
import json

app = FastAPI()
router = APIRouter(prefix="/api/v1")

templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")

# URI de connexion avec authentification

client = MongoClient(f'mongodb://admin:admin@mongodb:27017/')

db = client['DevOpsDB']  # Remplacez par le nom de votre base de données
collection = db['SpotifySongs']

all_songs = list(collection.find())
all_songs = clean_spotify_data_mongo(all_songs)


# df0=pd.read_csv('./data/spotify_data.csv')
# print(df0.iloc[14])

# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
# print(all_songs.iloc[0])
# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')


def fetc_img(id):
    url = f"https://embed.spotify.com/oembed?url=https://open.spotify.com/track/{id}"
    response = get(url)
    if response.status_code == 200:
        response_json = json.loads(response.content)    
        return response_json['thumbnail_url']


client = MongoClient("mongodb://admin:admin@mongodb:27017/")
db = client["DevOpsDB"]
collection = db["SpotifySongs"]
# Configuration des templates
templates = Jinja2Templates(directory="templates")

@router.get("/random")
async def random(request: Request,):
    input_song =all_songs.sample(n=1).iloc[0]
    print(input_song)
    img_uri = fetc_img(input_song.id)
    playlist = generate_playlist(all_songs, input_song, 10)
    playlist = playlist[1:10]  
    # Passer la playlist au template HTML

    return templates.TemplateResponse("out.html", {"request": request , "playlist": playlist , "input_song":input_song , "image": img_uri})

# Endpoint pour générer la playlist
@router.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, query: Optional[str] = Form(None)):
    filtered_songs = all_songs[all_songs['trackName'].notna() & all_songs['trackName'].str.contains(query, case=False)]

    if not filtered_songs.empty:
        input_song = filtered_songs.iloc[0]
        img_uri = fetc_img(img_uri)
        playlist = generate_playlist(all_songs, input_song, 10)
        playlist = playlist[1:10]  
        return templates.TemplateResponse("out.html", {"request": request, "playlist": playlist , "input_song":input_song , "image": img_uri})
    else:
        return templates.TemplateResponse("err.html" , {"request": request, "message": "song introuvable"})
   
    
@router.post("/get_track_infos")
async def predict(request: Request, track_id: str = Form(...)):
    infos_track = get_audio_features(track_id)
    
    features = list(infos_track.keys())
    
    playlist = generate_playlist(all_songs, infos_track, 9, features)
    return {"message": playlist}

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
