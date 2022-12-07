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
    import requests
    i = 0
    suggestion_json = requests.get(f"https://api.lyrics.ovh/suggest/{song_to_search})").json()
    song_name_api = suggestion_json["data"][i]["title"]
    singer = suggestion_json["data"][i]["artist"]["name"]
    
    
    cover_image = suggestion_json["data"][i]["album"]["cover_big"]
    cover_image = cover_image.replace("http", "https")   ## replace http with HTTPS


    lyrics_api = requests.get(f"https://api.lyrics.ovh/v1/{singer}/{song_name_api}").json()

    #return lyrics_api["lyrics"].split("\r")[1], song_name_api, singer, cover_image
    return song_name_api, singer, cover_image, suggestion_json["data"][i]

#print(main_request("senorita"))



def auto_complete(term_entered):
    auto_complete_sug = requests.get(f"https://api.lyrics.ovh/suggest/{term_entered})").json()
    try:
        return auto_complete_sug["data"][0]["title"], auto_complete_sug["data"][0]["artist"]["name"]##, auto_complete_sug["data"][1]["title"], auto_complete_sug["data"][1]["artist"]["name"], auto_complete_sug["data"][2]["title"], auto_complete_sug["data"][2]["artist"]["name"], auto_complete_sug["data"][3]["title"], auto_complete_sug["data"][3]["artist"]["name"] 
    except IndexError:
        print("ha")
        return "error", "error"





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