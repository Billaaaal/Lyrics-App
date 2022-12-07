import requests


def main_request(song_to_search):
    song_to_search = song_to_search.split(' (')
    singer = song_to_search[1].split(')')[0]
    song_to_search = song_to_search[0]
    #i = 0
    #suggestion_json = requests.get(f"https://api.lyrics.ovh/suggest/{song_to_search})").json()
    #song_name_api = suggestion_json["data"][i]["title"]
    #singer = suggestion_json["data"][i]["artist"]["name"]
    #while True:
    #    if suggestion_json["data"][i]["artist"]["name"] == singer:
    #        #singere = suggestion_json["data"][i]["artist"]["name"]
    #        break
    #    else:
    #        i = i+1

    #song_name_api = suggestion_json["data"][i]["title"]
    #singer = suggestion_json["data"][i]["artist"]["name"]
    
    #cover_image = suggestion_json["data"][i]["album"]["cover_big"]
    #cover_image = cover_image.replace("http", "https")   ## replace http with HTTPS


    #lyrics_api = requests.get(f"https://api.lyrics.ovh/v1/{singer}/{song_name_api}").json()

    url = "https://genius.p.rapidapi.com/search"

    querystring = {"q":song_to_search}

    headers = {
    'x-rapidapi-host': "genius.p.rapidapi.com",
    'x-rapidapi-key': "56a3c9d66emsh1548a3d26741d44p11469fjsn2268a9553b1e"
    }
    
    i = 0


    

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    #print(song_to_search.lower())
    #print(response["response"]["hits"][0]["result"]["title"].lower())

    #print(response["response"]["hits"][ia]["result"]["title"].lower())


    #if response["response"]["hits"][i]["result"]["header_image_url"]

    #print(song_to_search) #response["response"]["hits"][1]["result"]["title"].lower())
    
    i = 0
    try:
        while True:
            if response["response"]["hits"][i]["result"]["title"].lower() == song_to_search.lower() and response["response"]["hits"][i]["result"]["artist_names"].lower() == singer.lower():
                song_name_api = response["response"]["hits"][i]["result"]["title"]
                singer = response["response"]["hits"][i]["result"]["artist_names"]
                cover_image = response["response"]["hits"][i]["result"]["song_art_image_url"]
                break
            else:
                i = i+1
    except IndexError:
        return "Erreur"        



    lyrics_api = requests.get(f"https://api.lyrics.ovh/v1/{singer}/{song_name_api}").json()

    lyrics = lyrics_api["lyrics"].split("\r")
    lyrics = ''.join(lyrics)

    #return lyrics_api["lyrics"].split("\r")[1], "song_name_api", "singer", "cover_image"
    return lyrics, song_name_api, singer, cover_image

#print(main_request("shape of you (Ed Sheeran)"))





















def auto_complete(term_to_search):
    url = "https://genius.p.rapidapi.com/search"

    querystring = {"q":term_to_search}

    headers = {
    'x-rapidapi-host': "genius.p.rapidapi.com",
    'x-rapidapi-key': "56a3c9d66emsh1548a3d26741d44p11469fjsn2268a9553b1e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()



    
    try:
        song1_song = response["response"]["hits"][0]["result"]["title"]
        song1_singer = response["response"]["hits"][0]["result"]["primary_artist"]["name"]
    except IndexError:
        return "Erreur"

    
    try:
        song2_song = response["response"]["hits"][1]["result"]["title"]
        song2_singer = response["response"]["hits"][1]["result"]["primary_artist"]["name"]
    except IndexError:
        return "Erreur"


    try:
        song3_song = response["response"]["hits"][2]["result"]["title"]
        song3_singer = response["response"]["hits"][2]["result"]["primary_artist"]["name"]
    except IndexError:
        return "Erreur"
    
    return song1_song, song1_singer, song2_song, song2_singer, song3_song, song3_singer #####ajouter l'image car l'api n°1 ne fonctionne plus


#print(auto_complete("you'll never"))

    