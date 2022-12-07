import requests
#def main_request():

    #import requests, json
    #from datetime import date
    #import datetime
    #import locale
    
    ##import lyricsgenius
    ####genius = lyricsgenius.Genius("F1kUSDfmkThcvLzkgoWc08iZkzklGWhHHb4rRY6S_Kb4f7dnC130VuHvohfSJuPp")

    #api_key = "270c91bb046e4c35af0c1666b7d180e4"

    #request_url = f"https://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey={api_key}"
    #response = requests.get(request_url)
    #x = response.json()
    #print(request_url)
    #return x

    #locale.setlocale(
        #category=locale.LC_ALL,
        #locale="French"  
    #)
    #dateee = str(datetime.datetime.now())
    #year, month, day = dateee.split("-") 
    #day, rest = day.split(" ")

    #day = int(day)
    #month = int(month)
    #year = int(year)

    #the_date = date(day=day, month=month, year=year).strftime('%d %B %Y').title()

    #if "January" in the_date:
    #    the_date = the_date.replace("january", "janvier")
    #elif "February" in the_date:
    #    the_date = the_date.replace("February", "février")
    #elif "March" in the_date:
    #    the_date = the_date.replace("March", "Mars")
    #elif "April" in the_date:
    #    the_date = the_date.replace("April", "Avril")
    #elif "May" in the_date:
    #    the_date = the_date.replace("May", "Mai")
    #elif "June" in the_date:
    #    the_date = the_date.replace("June", "Juin")
    #elif "July" in the_date:
    #    the_date = the_date.replace("July", "Juillet")
    


    #date_o_the_day = f"Aujourd'hui, nous sommes le {the_date}"

    #return date_o_the_day

    #baseUrl = "http://api.genius.com"

    #headers = {'Authorization': 'Bearer F1kUSDfmkThcvLzkgoWc08iZkzklGWhHHb4rRY6S_Kb4f7dnC130VuHvohfSJuPp'}
    #searchUrl = baseUrl + "/search"
    #songTitle = "Shape of you"
    #data = {'q': songTitle}
    #response = requests.get(searchUrl, params=data, headers=headers)
    
    #x = response.json()

    ########song = genius.search_song("Shape of you")
    
    ########print(song.lyrics)


    #i = 0
    #while True:
    #    if x["articles"][i]["urlToImage"] == None:
    #        i = i+1
    #    else:
    #        val = x["articles"][i]["urlToImage"]
    #        break
    
    #while True:
    #    if "http" not in str(x["articles"][i]["urlToImage"]):
    #        i = i+1
    #    else:
    #        val = x["articles"][i]["urlToImage"]
    #        break

        



    
    #return x["articles"][0]["urlToImage"]
    #return val
    
########main_request()

##print(main_request())




#def main_request(song_to_search):
#    import lyricsgenius
#    genius = lyricsgenius.Genius("F1kUSDfmkThcvLzkgoWc08iZkzklGWhHHb4rRY6S_Kb4f7dnC130VuHvohfSJuPp")
#    song = genius.search_song(song_to_search)
#    return song.lyrics


def main_request(song_to_search):
    song_to_search = song_to_search.split('(')
    singer = song_to_search[1].split(')')[0]
    i = 0
    suggestion_json = requests.get(f"https://api.lyrics.ovh/suggest/{song_to_search})").json()
    #song_name_api = suggestion_json["data"][i]["title"]
    #singer = suggestion_json["data"][i]["artist"]["name"]
    while True:
        if suggestion_json["data"][i]["artist"]["name"] == singer:
            #singere = suggestion_json["data"][i]["artist"]["name"]
            break
        else:
            i = i+1

    song_name_api = suggestion_json["data"][i]["title"]
    singer = suggestion_json["data"][i]["artist"]["name"]
    
    cover_image = suggestion_json["data"][i]["album"]["cover_big"]
    cover_image = cover_image.replace("http", "https")   ## replace http with HTTPS


    lyrics_api = requests.get(f"https://api.lyrics.ovh/v1/{singer}/{song_name_api}").json()

    return lyrics_api["lyrics"].split("\r")[1], song_name_api, singer, cover_image
    #return lyrics_api["lyrics"].split("\r")[1], song_name_api, singer, cover_image

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
    
    return song1_song, song1_singer, song2_song, song2_singer, song3_song, song3_singer

print(auto_complete("shape of you"))


def auto_completee(term_to_search):
    url = "https://genius.p.rapidapi.com/search"

    querystring = {"q":"Kendrick Lamar"}

    headers = {
    'x-rapidapi-host': "genius.p.rapidapi.com",
    'x-rapidapi-key': "56a3c9d66emsh1548a3d26741d44p11469fjsn2268a9553b1e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    song1_song = response["response"]["hits"][0]["result"]["title"]
    song1_singer = response["response"]["hits"][0]["result"]["primary_artist"]["name"]
    return song1_song, song1_singer



#print(auto_complete("Shape of you"))


def auto_complete_e(term_to_search):
    suggestion_json_auto_complete = requests.get(f"https://api.lyrics.ovh/suggest/{term_to_search})").json()

    #ajouter un for loop sur suggestion_json_auto_complete["data"]

    #for song in suggestion_json_auto_complete["data"]:
    #    print(song)
    
    try:
        song1_song = suggestion_json_auto_complete["data"][0]["title"]
        song1_singer = suggestion_json_auto_complete["data"][0]["artist"]["name"]
    except IndexError:
        return "Erreur"

    
    try:
        song2_song = suggestion_json_auto_complete["data"][1]["title"]
        song2_singer = suggestion_json_auto_complete["data"][1]["artist"]["name"]
    except IndexError:
        return "Erreur"


    try:
        song3_song = suggestion_json_auto_complete["data"][2]["title"]
        song3_singer = suggestion_json_auto_complete["data"][2]["artist"]["name"]
    except IndexError:
        return "Erreur"
    
    return song1_song, song1_singer, song2_song, song2_singer, song3_song, song3_singer



















#import webbrowser
#import time

def auto_completeeuuh(term_to_search):
    suggestion_json_auto_complete = requests.get(f"https://api.lyrics.ovh/suggest/{term_to_search})").json()

    #ajouter un for loop sur suggestion_json_auto_complete["data"]
    list = []
    for song in suggestion_json_auto_complete["data"]:
        #print(song)
        list.append((song["title"],song["artist"]["name"], song["album"]["cover_big"]))
    #    webbrowser.open(song["album"]["cover_big"])

    #for song in list:
    #    webbrowser.open(song[2])
    #    time.sleep(0.5)
    #print(list)

#auto_completeeuuh("shape of you")









def main_request___(song_to_search):
    suggestion_json = requests.get(f"https://api.lyrics.ovh/suggest/{song_to_search})").json()
    

    song_name_api = suggestion_json["data"][0]["title"]
    singer = suggestion_json["data"][0]["artist"]["name"]

    lyrics_api = requests.get(f"https://api.lyrics.ovh/v1/{singer}/{song_name_api}").json()

    lyrics_split = lyrics_api["lyrics"].split("\r")[1].split("\n\n")

    for paragraphs in lyrics_split:
        for lign in paragraphs.split("\n"):
            if len(lign) - lign.count("\n\n"):
                he =  lign[:48], lign[len(lign)-48:]
                print(he)
            
                
            
            
                print("Hello World")




    #ne pas oublier de rajouter "\n\n" à la fin de chaque phrase

    

    #return lyrics_api["lyrics"].split("\r")[1], song_name_api, singer

    #return lyrics_split