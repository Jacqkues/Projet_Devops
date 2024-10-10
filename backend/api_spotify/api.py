
import base64
import os
from requests import post, get
import json



#client_id = os.getenv("CLIENT_ID")
#client_secret = os.getenv("CLIENT_SECRET")
client_id ="2ea0c513788c48ea9feedf19fc5e77c9"
client_secret = "f0da29e9364046b6b717d43266fb08b7"
def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = post(url, headers=headers, data=data) 
    response_json = json.loads(response.content)
    token = response_json["access_token"]
    
    return token

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def get_artist_id(artist_name):
    token = get_token()
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1&market=FR"
    
    query_url = url + query
    response = get(query_url, headers=headers)
    
    if response.status_code == 200:
        response_json = json.loads(response.content)
        if response_json['artists']['items']:
            return response_json['artists']['items'][0]['id']
        else:
            print("Artiste non trouvé.")
            return None
    else:
        print(f"Erreur {response.status_code}: {response.content}")
        return None

def get_artist_tracks(artist_id):
    token = get_token()
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=FR"
    headers = get_auth_header(token)
    
    response = get(url, headers=headers)
    
    if response.status_code == 200:
        response_json = json.loads(response.content)
        return response_json['tracks'][:5]
    else:
        print(f"Erreur {response.status_code}: {response.content}")
        return None
    
def search_by_track(track, market="FR"):
    token = get_token()
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q=track:{track}&type=track&limit=9&market={market}"
    
    query_url = url + query
    response = get(query_url, headers=headers)
    
    if response.status_code == 200:
        response_json = json.loads(response.content)
        tracks = response_json['tracks']['items']
        return tracks
    else:
        print(f"Erreur {response.status_code}: {response.content}")

def search_by_artist(artist):
    artist_id = get_artist_id(artist)
    if artist_id:
        tracks = get_artist_tracks(artist_id)
        if tracks:
            print(f"Top tracks de {artist}:")
            for track in tracks:
                print(f"- {track['name']} (Popularité: {track['popularity']})")
            return tracks
    else:    
        print("Artiste non trouvé.")

def search_by_track_and_artist(track, artist, market="FR"):
    token = get_token()
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q=track:{track} artist:{artist}&type=track&limit=5&market={market}"
    
    query_url = url + query
    response = get(query_url, headers=headers)
    
    if response.status_code == 200:
        response_json = json.loads(response.content)
        tracks = response_json['tracks']['items']
        for track in tracks:
            print(f"- {track['name']}, (Artiste: {track['artists'][0]['name']}) (Popularité: {track['popularity']})")
        return tracks
    else:
        print(f"Erreur {response.status_code}: {response.content}")

def get_audio_features(track_id):
    token = get_token()
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = get_auth_header(token)
    response = get(url, headers=headers)

    if response.status_code == 200:
        audio_features_json = json.loads(response.content)

        numerical_features = {
            'danceability': audio_features_json['danceability'],
            'energy': audio_features_json['energy'],
            'key': audio_features_json['key'],
            'loudness': audio_features_json['loudness'],
            'mode': audio_features_json['mode'],
            'speechiness': audio_features_json['speechiness'],
            'acousticness': audio_features_json['acousticness'],
            'instrumentalness': audio_features_json['instrumentalness'],
            'liveness': audio_features_json['liveness'],
            'valence': audio_features_json['valence'],
        }

        return numerical_features
    
    else:
        return {"error": response.status_code, "message": response.text}
    
def get_infos_track(track_id):
    token = get_token()
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    response = get(url, headers=headers)

    if response.status_code == 200:
        track_infos_json = json.loads(response.content)
        
        infos_track = {
            'id': track_id,
            'trackName': track_infos_json['name'],
            'artistName': track_infos_json['artists'][0]['name'],
        }

        return infos_track